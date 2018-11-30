# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tags(models.Model):
    name=models.CharField(max_length = 250)
    def __unicode__(self):
        return  self.name

class Category(models.Model):
    name=models.CharField(max_length = 250)
    def __unicode__(self):
        return  self.name
    
class News(models.Model):
    tags=models.ManyToManyField(Tags)
    category=models.ForeignKey(Category, verbose_name=u'Базовая категория', null=True, blank=True)
    title = models.CharField(max_length = 250)
    content = models.TextField()
    urls = models.CharField(max_length = 250)
    photo = models.ImageField(upload_to='catalog_pic/', null=True, blank=True, verbose_name='Photo')

    is_pub=models.BooleanField(verbose_name="Опубликовать", default=False)

    pressa_share = models.PositiveIntegerField(verbose_name='page', default="1")
    

    def __unicode__(self):
        return  self.title

    
