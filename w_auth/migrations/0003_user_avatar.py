# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_auth', '0002_auto_20170722_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='/static/upload/default_avatar.jpeg', max_length=150, null=True),
        ),
    ]
