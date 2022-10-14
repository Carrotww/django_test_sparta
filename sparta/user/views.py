from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        
        user_table = UserModel()
        user_table.username = username
        user_table.password = password
        user_table.phone = phone
        user_table.address = address
        user_table.save()

        return redirect('/login')
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is not None:
            print('성공')
            return redirect('/home')
        else:
            print('????')
            return redirect('/login')
    else:
        return render(request, 'login.html')

@login_required
def home(request):
   if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'home.html')
        else:
            return redirect('/login')