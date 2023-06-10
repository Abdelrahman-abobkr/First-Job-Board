from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .froms import *
from .models import Profile
from jobs.decorators import *
# Create your views here.



@user_authenticate
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Is Already Exist')
            return redirect('register')
        else:
            if form.is_valid():
                form.save()
                return redirect('login')
    return render(request, 'registration/register.html', {'form':form})



@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile':profile
    }
    return render(request, 'profile.html', context)



@login_required(login_url='login')
def edit(request):
    profile = Profile.objects.get(user=request.user)
    p_form = ProfileForm(instance=profile)
    u_form = UserForm(instance=request.user)
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, instance=profile)
        u_form = UserForm(request.POST, instance=request.user)
        if p_form and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('profile')
    context = {
        'p_form' : p_form,
        'u_form' : u_form
    }
    return render(request, 'edit.html', context)