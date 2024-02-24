from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1','password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
            
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class FlightSearchForm(forms.Form):
    departure_airport = forms.ModelChoiceField(queryset=Airport.objects.all(), empty_label=None, label='Departure Airport')
    destination_airport = forms.ModelChoiceField(queryset=Airport.objects.all(), empty_label=None, label='Destination Airport')
    departure_date = forms.DateField(label='Departure Date', widget=forms.DateInput(attrs={'type': 'date'}))
    departure_time_range = forms.ChoiceField(choices=[('morning', 'Morning (6:00 AM - 12:00 PM)'),
                                                      ('afternoon', 'Afternoon (12:00 PM - 6:00 PM)'),
                                                      ('evening', 'Evening (6:00 PM - 12:00 AM)')],
                                             label='Departure Time Range')

