from django.db import models


class User(models.Model):
    room_name = models.CharField(max_length=30,primary_key=True)
    is_open = models.BooleanField()








