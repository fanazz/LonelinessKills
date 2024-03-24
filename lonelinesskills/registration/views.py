from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import models
from .forms import RegistrationForm, LonelyHumanProfileForm, VolunteerProfileForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _("Thank you! On other step you will choose why you come on this website and fill other information."))
            return redirect('choose_profile_type')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {
        'form': form
        })

@login_required
def choose_profile_type(request:HttpRequest) ->HttpResponse:
    if request.method == "POST":
        profile_type = request.POST.get("profile_type")
        if profile_type == "lonelyhuman":
            return redirect('create_lonelyhuman_profile')
        elif profile_type == "volunteer":
            return redirect('create_volunteer_profile')
    return render(request, 'choose_profile_type.html')

@login_required
def create_lonely_human_profile(request:HttpRequest) ->HttpResponse:
    if request.method == "POST":
        lonely_human_profile_form = LonelyHumanProfileForm(request.POST)
        if lonely_human_profile_form.is_valid():
            instance = lonely_human_profile_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, _("Good job, we get your information and then will appear volunteer who matches your requirements it will contact with you as soon as posible."))
            return redirect('home')
    else:
        lonely_human_profile_form = LonelyHumanProfileForm()
                    
    context = {
        'page_ref': 'create_lonelyhuman_profile',
        'profile_form': lonely_human_profile_form,
    }
    return render(request, 'create_profile.html', context)

@login_required
def create_volunteer_profile(request:HttpRequest) ->HttpResponse:
    if request.method == "POST":
        volunteer_profile_form = VolunteerProfileForm(request.POST)
        if volunteer_profile_form.is_valid():
            instance = volunteer_profile_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, _("Thank you for your kindness! Now you you have to choose one person he needs you."))
            return redirect('home')
    else:
        volunteer_profile_form = VolunteerProfileForm()
                    
    context = {
        'page_ref': 'create_volunteer_profile',
        'profile_form': volunteer_profile_form,
    }
    return render(request, 'create_profile.html', context)