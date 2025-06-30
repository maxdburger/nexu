from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # check if registration valid

        if not email or not password1 or not password2:
            messages.error(request, 'Please fill out all fields')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'account already exists, please log in')
        else:
            User.objects.create_user(username=email, email=email, password=password1)

            authenticated_user = authenticate(request, username=email, password=password1)

            login(request, authenticated_user)
            return redirect('landing')

    return render(request, 'sign-up.html')

def logout_view(request):
    logout(request)
    return redirect('landing')

def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please fill out all fields')
        elif not User.objects.filter(email=email).exists():
            messages.error(request, 'Email does not exist')
        elif authenticate(request, username=email, password=password):
            login(request, authenticate(request, username=email, password=password))
            return redirect('landing')
        else:
            messages.error(request, 'Wrong password. Try again')


    return render(request, 'log-in.html')
