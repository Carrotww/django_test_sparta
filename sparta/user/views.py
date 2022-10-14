from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        user_table = UserModel()
        user_table.username = request.POST.get('username')
        user_table.set_password(request.POST.get('password'))
        user_table.phone = request.POST.get('phone')
        user_table.address = request.POST.get('address')

        user_table.save()

        return redirect('/login')
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is not None:
            auth.login(request, user)
            print('성공')
            return redirect('/home')
        else:
            print('????')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def home(request):
    user = request.user.is_authenticated
    if user:
        print('user')
        return render(request, 'home.html')
    else:
        print('login')
        return redirect('/login')