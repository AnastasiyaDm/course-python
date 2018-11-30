# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181126_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='main.Tags'),
        ),
    ]