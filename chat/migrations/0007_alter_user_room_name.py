# Generated by Django 3.2.6 on 2021-08-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_user_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room_name',
            field=models.UUIDField(default='NJR3HPFN377A3H6O52H2SGIEMP4J9G', editable=False, primary_key=True, serialize=False),
        ),
    ]
