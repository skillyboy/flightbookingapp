from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # User URLs

    path('signup/', views.signupform, name='signupform'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),

    path('', views.dashboard, name='dashboard'),

    # Search Flights
    path('search_flights/', SearchFlightsView.as_view(), name='search_flights'),

    # Book Flight
    path('book/<int:flight_id>/', BookFlightView.as_view(), name='book_flight'),

    # My Bookings
    path('mybookings/', MyBookingsView.as_view(), name='mybookings'),


    # View Bookings
    path('my_bookings/', ViewBookingsView.as_view(), name='my_bookings'),
]
