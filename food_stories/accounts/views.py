from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView

from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from accounts.tasks import send_confirmation_mail
from accounts.utils.tokens import account_activation_token
from stories.models import Story, Recipe

User = get_user_model()


def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            send_confirmation_mail(user)
            return redirect(reverse_lazy('accounts:login'))
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


def logout(request):
    django_logout(request)
    messages.success(request, 'You are logout')
    return redirect(reverse_lazy('stories:index'))


def activate(request, uidb64, token):

    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your account activated')
        user.is_active = True
        user.save()
        return redirect('accounts:login')
    else:
        messages.error(request, 'your link expired or link invalid')
        return redirect('stories:index')


# class UserProfileListView(ListView):
#     # model = Story
#     queryset = Story.objects.filter(is_published=True)
#     template_name = 'user-profile.html'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(author=self.request.user)
#
#     def get_context_data(self, **kwargs):
#         context = super(UserProfileListView, self).get_context_data(**kwargs)
#         context['recipe_list'] = Recipe.objects.filter(author=self.request.user, is_published=True)
#         return context

class UserProfileView(DetailView):
    model = User
    template_name = 'user-profile.html'
    context_object_name = 'user_object'

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileListView, self).get_context_data(**kwargs)
    #     context['recipe_list'] = Recipe.objects.filter(author=self.request.user, is_published=True)
    #     return context
