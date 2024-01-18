import json
from django.shortcuts import render
from .models import UserData


def signup(request):
    return render(request, 'login/signup.html')


def login(request):
    return render(request, 'login/login.html')


def store_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if username and password and re_password:
            if password != re_password:
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Password not matching', 'password': ''}})
            try:
                user = UserData.objects.get(username=username)
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Already present', 'password': ''}})
            except UserData.DoesNotExist:
                UserData.objects.create(username=username, password=password)
                return render(request, 'login/signup.html', {'context': {'username': username, 'password': password}})
    return render(request, 'login/signup.html', {'context': {'username': '', 'password': ''}})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = UserData.objects.get(username=username)
                if user.password == password:
                    return render(request, 'login/login.html', {'context': {'username': 'Match', 'password': ''}})
                else:
                    return render(request, 'login/login.html', {'context': {'username': 'Not Match', 'password': ''}})
            except UserData.DoesNotExist:
                return render(request, 'login/login.html', {'context': {'username': 'Invalid Username', 'password': ''}})
    return render(request, 'login/login.html', {'context': {'username': '', 'password': ''}})

