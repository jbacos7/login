# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['product_id'] == '1':
            quantity = int(request.POST['quantity'])
            charge = quantity * 699.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '2':
            quantity = int(request.POST['quantity'])
            charge = quantity * 13399.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '3':
            quantity = int(request.POST['quantity'])
            charge = quantity * 359.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '4':
            quantity = int(request.POST['quantity'])
            charge = quantity * 32.99
            request.session['charge'] = charge

        if not 'item_count' in request.session:
            request.session['item_count'] = 0
        count = request.session['item_count']
        count += quantity
        request.session['item_count'] = count

        if not 'total_charge' in request.session:
            request.session['total_charge'] = 0
        total_charge = request.session['total_charge']
        total_charge += charge
        request.session['total_charge'] = total_charge
        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'checkout.html')

def reset(request):
    request.session.clear()
    return redirect('/')