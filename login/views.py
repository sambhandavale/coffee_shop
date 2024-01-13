import json
from django.shortcuts import render
import pandas as pd
import os


def signup(request):
    return render(request, 'login/signup.html')


def login(request):
    return render(request, 'login/login.html')


def store_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        data = {
            'context': {'username': username, 'password': password}
        }
        if username and password and re_password:
            if password != re_password:
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Password not matching', 'password': ''}})
            path = os.getcwd()
            csv_file_path = path + r'\user_data.csv'
            df = pd.read_csv(csv_file_path)
            if username in list(df.usernames):
                return render(request, 'login/signup.html',
                              {'context': {'username': 'Already present', 'password': ''}})
            else:
                new_data = pd.DataFrame({'usernames': [username], 'passwords': [password]})
                df = pd.concat([df, new_data], ignore_index=True)
                df.to_csv(csv_file_path, index=False)
                return render(request, 'login/signup.html', data)
    return render(request, 'login/signup.html', {'context': {'username': '', 'password': ''}})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            og_path = os.getcwd()
            parent_path = os.path.dirname(og_path)
            csv_file_path = parent_path+r'\coffee_shop\user_data.csv'
            df = pd.read_csv(csv_file_path)
            if username in list(df.usernames):
                index = df[df['usernames'] == username].index[0]  # to find the index of the row
                if str(df.loc[index, 'passwords']) == str(password):
                    return render(request, 'login/login.html', {'context': {'username': 'Match', 'password': ''}})
                else:
                    return render(request, 'login/login.html', {'context': {'username': 'Not Match', 'password': ''}})
            else:
                return render(request, 'login/login.html',
                              {'context': {'username': 'Invalid Username', 'password': ''}})
    return render(request, 'login/login.html', {'context': {'username': '', 'password': ''}})


a = os.getcwd()
b = os.path.dirname(a)
