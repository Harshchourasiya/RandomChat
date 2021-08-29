from asyncio.windows_events import NULL
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import User


class MyConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'connect_message',
                'message': str(User.objects.get(room_name=self.room_name).is_open)
            })

    def receive(self, text_data):

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'message': text_data
            }
        )

    def disconnect(self, *args, **kwargs):
        user = User.objects.get(room_name=self.room_name)
        user.delete()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'disconnect_message',
                'message': 'Yes'
            })
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

# Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def connect_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'connect': message
        }))

    def disconnect_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'connect': 'True',
            'disconnect': message
        }))
