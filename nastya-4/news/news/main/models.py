# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField()
    link = models.CharField(max_length = 512)

    def __unicode__(self):
        return self.title
