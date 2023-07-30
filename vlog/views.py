# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('dashboard')  # Redirect to the dashboard page after registration

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page upon successful login

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logging out


def dashboard_view(request):
    return render(request, 'dashboard.html')
