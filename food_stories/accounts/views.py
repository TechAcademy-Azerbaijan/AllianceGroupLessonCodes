from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as django_login


def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user:
                django_login(request, user)
                messages.success(request, 'You are logged in')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)