# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    #pass
    list_display=('title','content')
    list_filter=('tags',)
    search_fields=('title',)
   
admin.site.register(News,NewsAdmin)

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tags,TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)
