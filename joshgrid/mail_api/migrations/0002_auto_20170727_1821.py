# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'ordering': ('time_created', 'sender')},
        ),
        migrations.RenameField(
            model_name='mail',
            old_name='sender_name',
            new_name='sender',
        ),
    ]
