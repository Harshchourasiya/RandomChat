"""
ASGI config for omega project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import  re_path
from chat.consumers import MyConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omega.settings')

application = get_asgi_application()

ws_patterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', MyConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(ws_patterns))
})

