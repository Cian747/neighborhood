from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from itertools import chain



# Create your views here.

def register_user(request):
    rgf =RegistrationForm()
    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_user')
    
    return render(request, 'registration/registration.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login_user')