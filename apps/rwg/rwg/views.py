# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
import string
import random

# Create your views here.


def index(request):
    return render(request, 'index.html')


def randword(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    request.session['attempt'] = request.session['attempt'] + 1
    context = {
        "random_word": ''.join(random.choice(string.ascii_uppercase) for _ in range(14)),
        "attempt": request.session['attempt']
    }
    return render(request, 'index.html', context)
