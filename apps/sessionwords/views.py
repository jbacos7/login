# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        #date = datetime.now().strftime('%-I:%-M:%S%p, %b %D %Y')
        content = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': request.POST['big'],
        #'added': str(date)
        }
        if not 'list' in request.session:
            request.session['list'] = []
        saved_list = request.session['list']
        saved_list.append(content)
        request.session['list'] = saved_list
        print request.session['list']
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')