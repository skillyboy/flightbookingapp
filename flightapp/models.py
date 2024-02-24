from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# from db_connection import db

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)

    def __str__(self):
        return self.model

class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=20, unique=True)
    origin = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    available_seats = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"{self.airline.name} - {self.flight_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"
