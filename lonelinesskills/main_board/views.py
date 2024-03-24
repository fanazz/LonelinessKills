from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from registration.models import VolunteerProfile, LonelyHumanProfile



def index(request: HttpRequest) -> HttpResponse:
    context = {
        'volunteer_count': VolunteerProfile.objects.count(),
        'lonely_human_count': LonelyHumanProfile.objects.count()
    }
    return render(request, 'main_board/index.html', context)
