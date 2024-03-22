from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import models
from .forms import LonelyHumanRegistrationForm, LonelyHumanProfileForm, VolunteerRegistrationForm, VolunteerProfileForm


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'volunteer_count': models.VolunteerProfile.objects.count(),
        'lonely_human_count': models.LonelyHumanProfile.objects.count()
    }
    return render(request, 'registration/index.html', context)

def volunteer_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'registration/volunteer_list.html', {
        'volunteer_list': models.VolunteerProfile.objects.all(),
    })

def lonely_human_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'registration/lonely_human_list.html', {
        'lonely_human_list': models.LonelyHumanProfile.objects.all(),
    })

def lonely_human_register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LonelyHumanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Nice job, you registered, now you can log in with you credentials and fill another required information."))
            return redirect('login')
    else:
        form = LonelyHumanRegistrationForm()
    return render(request, 'registration/lonely_human_register.html', {
        'form': form,
    })

@login_required
def lonely_human_fill_information(request: HttpRequest) -> HttpResponse:
    lonely_human_profile = models.LonelyHumanProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = LonelyHumanProfileForm(request.POST, instance=lonely_human_profile)
        if form.is_valid():
            form.save()
            messages.success(request, _("Good job, we get your information and then will appear volunteer who matches your requirements it will contact with you as soon as posible."))
    else:
        form = LonelyHumanProfileForm(instance=lonely_human_profile)
    return render(request, 'registration/lonely_human_fill_information.html', {'form': form})

def volunteer_register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you for your kindness. Now you can log in with you credentials and fill another required information."))
            return redirect('login')
    else:
        form = VolunteerRegistrationForm()
    return render(request, 'volunteer_register.html', {
        'form': form
        })

@login_required    
def volunteer_fill_information(request: HttpRequest) -> HttpResponse:
    volunteer_profile = models.VolunteerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = VolunteerProfileForm(request.POST, instance=volunteer_profile)
        if form.is_valid():
            form.save()
            return redirect('lonely_human_list')  # Arba į bet kurį kitą page, kurį norite
    else:
        form = VolunteerProfileForm(instance=volunteer_profile)
    return render(request, 'volunteer_fill_information.html', {'form': form})


# def create_lonely_human_profile(request):
#     if request.method == 'POST':
#         form = LonelyHumanProfileForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             name = form.cleaned_data['name']
#             lonely_human = LonelyHuman.objects.create(username=username, name=name)
#             return redirect('update_profile', pk=lonely_human.pk)
#     else:
#         form = LonelyHumanProfileForm()
#     return render(request, 'create_profile.html', {'form': form})

# def update_profile(request, pk):
#     lonely_human = LonelyHuman.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = LonelyHumanForm(request.POST, instance=lonely_human)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_success')
#     else:
#         form = LonelyHumanForm(instance=lonely_human)
#     return render(request, 'update_profile.html', {'form': form})

# def profile_success(request):
#     return render(request, 'profile_success.html')