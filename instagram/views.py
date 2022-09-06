from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Profile
from .forms import UserRegisterForm, Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout ,authenticate


def feed(request):
    post = Post.objects.all()
    profile = Profile.objects.all()
    return render(request, 'instagram/feed.html', {'post': post, 'profile': profile})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect('/')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'instagram/register.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = Authentication(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Error')
    else:
        form = Authentication()
    return render(request, 'instagram/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('/')

def detail(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, 'instagram/detail.html', {'profile': profile})


