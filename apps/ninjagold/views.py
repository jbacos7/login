# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random


def index(request):
    if 'curGold' not in request.session:
        request.session['curGold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = ""

    return render(request, 'index.html')


def process_money(request):
    bldg = request.POST['building']
    curGold = request.session['curGold']
    newGold = 0

    if bldg == 'farm':
        newGold = random.randint(10, 20)

    elif bldg == 'cave':
        newGold = random.randint(5, 10)

    elif bldg == 'house':
        newGold = random.randint(2, 5)

    elif bldg == 'casino':
        newGold = random.randint(-50, 50)
    else:
        request.session['curGold'] = 0

    request.session['curGold'] += newGold
    request.session['activities'] += buildActivities(bldg, curGold, newGold)
    return redirect('/')


def buildActivities(bldg, cur, new):
    msg = ""
    i = datetime.now()
    if new < 0:
        msg = '<span class="lost"> Entered a ' + bldg + ' and lost ' + \
            str(new) + '... Ouch..' + \
            i.strftime('%Y/%m/%d %I:%M:%S%p') + '</span><br>'
    else:
        msg = '<span class="won"> Earned ' + \
            str(new) + ' gold from the ' + bldg + '! ' + \
            i.strftime('%Y/%m/%d %I:%M:%S%p') + '</span><br>'

    return msg


def reset(request):
    request.session.clear()
    return redirect('/')