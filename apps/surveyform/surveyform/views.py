# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')


def process(request):
    if request.POST['submit'] == 'submitted':
        if "count" not in request.session:
            request.session['count'] = 0
        request.session['count'] = request.session['count'] + 1
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        request.session['submitted'] = True
    else:
        if "count" in request.session:
            count = request.session['count']
        request.session.clear()
        request.session['count'] = count

    return redirect('/')