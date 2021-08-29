from django.shortcuts import render
from .models import User
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
import string


def home(request):
    return render(request, "index.html")


def index(request, room_name):
    key = User.objects.filter(room_name=room_name).first()
    if(key != None):
        return render(request, "chat.html", {'room_name': room_name})
    else:
        return render(request, "notfound.html")


def lobby(request):
    key = User.objects.filter(is_open=True)[:1]
    if(key):
        room_name = key.get().room_name
        response = redirect('/chat/'+room_name+'/')
        user = User.objects.get(room_name=room_name)
        user.is_open = False
        user.save()
        return response
    else:
        user = User.objects.create(is_open=True, room_name=get_random_string(
            30, allowed_chars=string.ascii_uppercase + string.digits))
        user.save()
        room_name = user.room_name
        response = redirect('/chat/'+room_name+'/')
        return response
