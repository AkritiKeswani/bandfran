from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.decorators.debug import sensitive_post_parameters, sensitive_variables
from django.contrib.auth.forms import AuthenticationForm

from .forms import MyUserCreationForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'bandfran/landing.html', {})  # FIXME: redirect to the home page
    else:
        return redirect('signup')


@sensitive_variables('user_instance')
@sensitive_post_parameters()
@transaction.atomic
def participant_signup(request):
    if request.user.is_authenticated and request.user.is_active:
        return redirect('index')

    if request.method == 'POST':
        creation_form = MyUserCreationForm(request.POST or None)

        if creation_form.is_valid():
            user_instance = creation_form.save()
            login(request, user_instance)
            messages.success(request, 'Your account was created successfully.')
            return render(request, 'bandfran/landing.html', {})  # FIXME: need to redirect to the real home page
        else:
            messages.error(request, 'There was an error creating the profile because:')
            logger.info("signup form invalidated.")
    else:
        creation_form = MyUserCreationForm(request.POST or None)
    return render(request, 'bandfran/signup.html',
                  {'page_name': 'Band Fran | Sign Up', 'creation': creation_form})


@transaction.atomic
@sensitive_post_parameters()
@sensitive_variables('username', 'password', 'user')
def participant_signin(request):
    if request.user.is_authenticated and request.user.is_active:
        return redirect('index')

    if request.method == 'POST':
        authentication_form = AuthenticationForm(request.POST or None)

        if authentication_form.is_valid():
            username = authentication_form.cleaned_data.get('username')
            password = authentication_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if not user:
                authentication_form.add_error(field='password', error='Incorrect password for the username.')
            else:
                login(request, user)
                return render(request, 'bandfran/landing.html', {})  # FIXME: need to redirect to the real home page
    else:
        authentication_form = AuthenticationForm(request.POST or None)

    return render(request, 'bandfran/login.html',
                  {'page_name': 'Life Nest | Sign In', 'authentication': authentication_form})


@login_required
def participant_signout(request):
    logout(request)
    return redirect('index')
