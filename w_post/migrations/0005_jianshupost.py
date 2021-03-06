# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_post', '0004_auto_20170723_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='JianShuPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('intro', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('author_id', models.IntegerField()),
            ],
        ),
    ]
