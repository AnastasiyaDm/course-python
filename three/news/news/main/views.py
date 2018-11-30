# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):
    news=News.objects.all()
    ctx={'name':'Nastya','news':news}
    return render(request,'index.html',ctx)

def detail(request,id):
    news=News.objects.get(id=id)
    return render(request,'detail.html',{'news':news})
