# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_news_adddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('addDate', models.DateTimeField(verbose_name='Date')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]