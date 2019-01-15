from django import forms
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from homepage.forms import SignUpForm, UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from applications.models import Application 
import datetime as dt
from datetime import datetime

# Create your views here.
def homepage(request):
    '''View function for home page of site'''
    overdue = []
    soon = []

    for application in Application.objects.filter(owner=request.user, status='p'):
        if application.deadline < dt.date.today():
            overdue.append(application)
        elif (application.deadline - dt.date.today()).days <= 7:
            soon.append(application)

    context = {
        'overdue': overdue,
        'soon': soon,
    }

    return render(request, 'homepage/homepage.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# class UserDetailView(generic.DetailView):
#     model: User


def edit_user(request):
    #template = "registrations/edit_user.html"
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user, initial={'first_name':user.first_name, 'last_name':user.last_name, 'username':user.username, 'email':user.email})
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.save()
            return redirect('homepage')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'registration/edit_user.html', {'form': form})
