from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import MainImage, SecondImage, ThirdImage
from django.contrib import messages

# Create your views here.

def index(request):
    firstimage = MainImage.objects.all()
    secondsection = SecondImage.objects.all()
    thirdsection = ThirdImage.objects.all()
    return render(request, 'core/index.html', {'firstimage':firstimage, 'secondsection':secondsection, 'thirdsection':thirdsection})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.save()
        messages.success(request, ('You are successfully registered!'))
        return redirect('/')
    return render(request, 'core/signup.html', )

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            
            return redirect('/')
        
        
    return render(request, 'core/login.html')

def signout(request):
    logout(request)
    messages.success(request, 'You are successfully logged out!')
    return redirect('myapp:index')