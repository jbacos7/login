# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
    "date": strftime("%Y-%m-%d", gmtime()),
    "time": strftime("%H:%M %p", gmtime()),
    }
    return render(request,'index.html', context)