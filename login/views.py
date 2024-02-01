from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if username and password and re_password:
            if password != re_password:
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Password not matching', 'password': ''}})
            try:
                user = User.objects.get(username=username)
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Already present', 'password': ''}})
            except User.DoesNotExist:
                User.objects.create(username=username, password=make_password(password))
                messages.success(request, f'Account Created for {username}')
                return render(request, 'login/login.html')
    return render(request, 'login/signup.html', {'context': {'username': '', 'password': ''}})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                profile = Profile.objects.get(user=user)
                profile.no_of_logins += 1
                profile.save()
            except Profile.DoesNotExist:
                pass
            return redirect('user_profile', username=username)
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login/login.html')
