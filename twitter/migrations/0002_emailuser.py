# Generated by Django 2.0.7 on 2018-08-25 06:11

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
