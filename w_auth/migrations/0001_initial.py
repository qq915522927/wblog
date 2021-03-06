# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtitle', models.CharField(default='未激活用户', max_length=20)),
                ('power', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemil', models.CharField(max_length=30)),
                ('role', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='w_auth.Role')),
            ],
        ),
    ]
