from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from . import models

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'volunteer_count': models.Volunteer.objects.count(),
        'lonely_human_count': models.LonelyHuman.objects.count()
    }
    return render(request, 'registration/index.html', context)

def volunteer_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'registration/volunteer_list.html', {
        'volunteer_list': models.Volunteer.objects.all(),
    })

def lonely_human_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'registration/lonely_human_list.html', {
        'lonely_human_list': models.LonelyHuman.objects.all(),
    })

# def signup(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = forms.CreateVolunteerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, _("Thank you! You can log in now with your credentials."))
#             return redirect("index")
#     else:
#         form = forms.CreateVolunteerForm()
#     return render(request, 'panel/signup.html', {
#         'form': form,
#     }) 