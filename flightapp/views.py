from django.views.generic import View
from django.http import JsonResponse
from django.views import View
import requests
import json

from urllib3 import Retry
# from django.http import HttpResponse
from . forms import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import FlightSearchForm
from django.contrib import messages
from django.http import HttpResponseServerError

from datetime import datetime, time 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flight, Booking

def signupform(request):
    reg = SignupForm()
    if request.method == 'POST':
        reg = SignupForm(request.POST)
        if reg.is_valid():
            new_user = reg.save()
            login(request, new_user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    context = {
        'reg': reg
    }

    return render (request,'signup.html', context)


def password(request):
    update = PasswordChangeForm(request.user)
    if request.method == 'POST':
        update = PasswordChangeForm(request.user, request.POST)
        if update.is_valid():
            user=update.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful!')
            return redirect('index')
        else:
            messages.error(request, update.errors)
            return redirect('password')

    context = {
        'update': update
    }

    return render(request, 'password.html', context)


def logoutfunc(request):
    logout(request)
    return redirect('login')

def loginfunc(request):  
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
        
    return render (request, 'login.html')

@login_required(login_url='/login')
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    
    context={
        'bookings': bookings
    }

    return render(request, 'dashboard.html', context)


# .........................................................


class SearchFlightsView(View):
    def get(self, request):
        form = FlightSearchForm(request.GET)
        context = {'form': form}
        
        if form.is_valid():
            try:
                date = form.cleaned_data['departure_date']
                time = form.cleaned_data['departure_time_range']
                time_ranges = {
                    'morning': ('06:00:00', '12:00:00'),
                    'afternoon': ('12:00:00', '18:00:00'),
                    'evening': ('18:00:00', '23:59:59'),
                }
                start_time, end_time = time_ranges.get(time, (None, None))
                
                if start_time and end_time:
                    flights = Flight.objects.filter(
                        departure_datetime__date=date,
                        departure_datetime__time__gte=start_time,
                        departure_datetime__time__lte=end_time
                    )
                    if flights.exists():
                        return render(request, 'flight_list.html', {'flights': flights})
                    else:
                        messages.warning(request, "No flights available for the selected date and time range.")
                else:
                    messages.error(request, "Invalid time range selected.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return HttpResponseServerError("Internal Server Error")
        
        context['allflights'] = Flight.objects.all()
        return render(request, 'search_flights.html', context)

class BookFlightView(LoginRequiredMixin, View):
    def post(self, request, flight_id):
        user = request.user
        flight = Flight.objects.get(id=flight_id)
        if flight.available_seats > 0:
            booking = Booking.objects.create(user=user, flight=flight)
            flight.available_seats -= 1
            flight.save()
            return redirect('dashboard')
        else:
            return redirect('search_flights')

class MyBookingsView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'my_bookings.html', {'bookings': bookings})

    def post(self, request):
        airline = request.POST.get('airline')
        aircraft = request.POST.get('aircraft')
        flight_number = request.POST.get('flight_number')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        departure_datetime = request.POST.get('departure_datetime')
        arrival_datetime = request.POST.get('arrival_datetime')
        available_seats = request.POST.get('available_seats')
        flight = Flight.objects.create(airline=airline, aircraft=aircraft, flight_number=flight_number,
                                       origin=origin, destination=destination, departure_datetime=departure_datetime,
                                       arrival_datetime=arrival_datetime, available_seats=available_seats)
        return redirect('admin_dashboard')

class ViewBookingsView(LoginRequiredMixin, View):
    def get(self, request):
        flight_number = request.GET.get('flight_number')
        departure_datetime = request.GET.get('departure_datetime')
        bookings = Booking.objects.filter(flight__flight_number=flight_number,
                                          flight__departure_datetime=departure_datetime)
        return render(request, 'view_bookings.html', {'bookings': bookings})
