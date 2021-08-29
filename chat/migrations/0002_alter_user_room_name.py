# Generated by Django 3.2.6 on 2021-08-27 05:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room_name',
            field=models.UUIDField(default=uuid.uuid3, editable=False, primary_key=True, serialize=False),
        ),
    ]