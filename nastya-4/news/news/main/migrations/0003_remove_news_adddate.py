# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='addDate',
        ),
    ]