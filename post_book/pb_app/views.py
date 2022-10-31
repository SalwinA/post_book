from django.shortcuts import render, redirect
from .models import user_profile, user_post
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def home(request):
    posts = user_post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required(login_url='signin')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username.username).exists():
                messages.info(request, 'Username cannot be used!')
                return redirect('signup')
            
            elif User.objects.filter(email.email).exists():
                messages.info(request, 'Email cannot be used!')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

        else:
            messages.info(request, 'Password not match!')
            return redirect('signup')
    
    else:
        return render(request, 'signup.html')


@login_required(login_url='signin')
def postupload(request):
    return HttpResponse('<h1>Upload</h1>')