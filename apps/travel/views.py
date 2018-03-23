# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Users, Trips

# Create your views here.
def index(request):
    
    if 'user_id' not in request.session:
        request.session['user_id'] = -1
    return render(request, "index.html")

def travels(request):
    try:
        user = Users.objects.get(id=request.session['user_id'])
        my_trips = Users.objects.get(id=request.session['user_id']).trips.all()
        other_travelers = Users.objects.exclude(id=request.session['user_id'])
        other_trips = []
        for item in other_travelers:
            for value in item.trips.all():
                other_trips.append({
                    "name": item.name,
                    "destination": value.destination,
                    "start_DT": value.start_DT,
                    "end_DT": value.end_DT,
                    "trip_id": value.id,
                })
        context = {
            "name": "{}".format(user.name),
            "user_id": request.session['user_id'],
            "my_trips": my_trips,
            "other_trips": other_trips,
        }
        return render(request, "travels.html", context)
    except ObjectDoesNotExist:
        messages.error(request, "User id unknown!!")
        return redirect("/")

def destination(request, trip_id):
    try:
        trip = Trips.objects.get(id=trip_id)
        context = {
            "trip": trip,
            "travelers": trip.travelers.all()
        }
        return render(request, "destination.html", context)
    except ObjectDoesNotExist:
        messages.error(request, "Trip id unknown!!")
        return redirect('/travels')

def addtravel(request):
    return render(request, "addtravel.html")

def checktravel(request):
    if request.method == "POST":
        post_data = {
                "destination": request.POST['destination'],
                "description": request.POST['description'],
                "start_DT": request.POST['start_DT'],
                "end_DT": request.POST['end_DT'],
                "user_id": request.session['user_id'],
        }
        result = Trips.objects.createTrip(post_data)
        if result[0]:
            print "@"*50
            for item in result[1]:
                print item
            print "@"*50
            return redirect("/travels")
        else:
            for item in result[1]:
                messages.error(request, item)
            return redirect("/travels/add")
def jointravel(request, trip_id):
    data = {
        "trip_id": trip_id,
        "user_id": request.session['user_id'],
    }
    result = Trips.objects.jointravel(data)
    if result[0]:
        return redirect('/travels')
    else:
        for item in result[1]:
            messages.error(request, item)
        return redirect('/travels')

def checkuser(request):
    if request.method == 'POST':
        # Register button
        if request.POST['form_type'] == "reg":
            post_data = {
                "name": request.POST['name'],
                "email": request.POST['email'],
                "password": request.POST['password'],
                "confirm_pswrd": request.POST['confirm_pswrd'],
            }
            result = Users.objects.createUser(post_data)
            if result[0]:
                request.session['user_id'] = result[1].id
                return redirect("/travels")
            else:
                for item in result[1]:
                    messages.error(request, item)
                return redirect("/")
        # Login button
        elif request.POST['form_type'] == "log":
            post_data = {
                "email": request.POST['email'],
                "password": request.POST['password'],
            }
            result = Users.objects.checkLogin(post_data)
            if result[0]:
                request.session['user_id'] = result[1].id
                return redirect("/travels")
            else:
                for item in result[1]:
                    messages.error(request, item)
                return redirect("/")
        else:
            messages.error(request, "Unknown form method request")
            return redirect("/")

def logout(request):
    request.session.clear()
    messages.error(request, "You are logged out.")
    return redirect('/')