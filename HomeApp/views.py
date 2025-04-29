from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError  # used in tyr and except loop
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'HomeApp/home.html')

def About(request):
    return render(request, 'HomeApp/About.html', {'About':About})

def Contact(request):
    return render(request, 'HomeApp/contact.html', {'Contacts': Contact})

