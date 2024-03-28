from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import models
from . import forms
from datetime import datetime

User = get_user_model()

def register_as_volunteer(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form_user = forms.VolunteerUserForm(request.POST)
        form_profile = forms.VolunteerProfileForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid():
            personal_no = form_profile.cleaned_data.get('personal_no')
            gender = form_profile.cleaned_data.get('gender')
            age_from_personal_no = calculate_age_from_personal_no(personal_no)
            age_from_form = form_profile.cleaned_data.get('age')
            if validate_personal_no(personal_no, gender) and age_from_personal_no == age_from_form:
                user = form_user.save()
                profile = form_profile.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, _("Thank you for your kindness!"))
                return redirect('login')
            else:
                messages.error(request, _("You are not real person. Please fill your correct information"))

        else:
            messages.error(request, _("Form data is invalid. Please check your input and try again."))
    else:
        form_user = forms.VolunteerUserForm()
        form_profile = forms.VolunteerProfileForm()
    return render(request, 'register.html', {
        'title': _("Registration for Volunteers"),
        'subtitle': _("Signup for LonelinessKILLs volunteers if you have enough time, " + 
                      "empathy and energy to help people who feels abandoned and lonely in their lifes"),
        'button_text': _("Register Volunteer Account"),
        'form_user': form_user,
        'form_profile': form_profile,
    })

def register_as_lonely_human(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form_user = forms.LonelyHumanUserForm(request.POST)
        form_profile = forms.LonelyHumanProfileForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid(): 
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, _("Good job, now you have to wait then someone will match your requirements and choose you"))
            return redirect('login')  
    else:
        form_user = forms.LonelyHumanUserForm()
        form_profile = forms.LonelyHumanProfileForm()
    return render(request, 'register.html', {
        'title': _("Registration for Lonely Humans"),
        'subtitle': _("Signup on LonelinessKILLs if you feel lonely and want to find somebody who accept you."),
        'button_text': _("Register LonelyHuman Account"),
        'form_user': form_user,
        'form_profile': form_profile,
    })

def validate_personal_no(personal_no, gender):
        if len(personal_no) != 11:
            return False
        if not personal_no.isdigit():
            return False
        if (personal_no[0] == '3' or personal_no[0] == '5') and gender != 'M':
            return False
        if (personal_no[0] == '4' or personal_no[0] == '6') and gender != 'F':
            return False
        multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        checksum = sum(int(personal_no[i]) * multipliers[i] for i in range(10))

        remainder = checksum % 11

        if remainder == 10:
            multipliers = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
            checksum = sum(int(personal_no[i]) * multipliers[i] for i in range(10))
            remainder = checksum % 11

        if remainder == int(personal_no[10]):
            return True
        else:
            return False

def calculate_age_from_personal_no(personal_no):
    birth_year = int(personal_no[1:3])
    birth_month = int(personal_no[3:5])
    birth_day = int(personal_no[5:7])
    
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    age = current_year - 1900 - birth_year
    if (birth_month > current_month) or (birth_month == current_month and birth_day > current_day):
        age -= 1

    return age

@login_required
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    return render(request, 'registration/user_detail.html', {
        'object': user,
    })




# def register(request:HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         if 'submit_volunteer' in request.POST:
#             form = forms.VolunteerRegistrationForm(request.POST)
#             role = Role.VOLUNTEER
#             success_message = _("Thank you for your kindness! Now you can login and have to fill additional information and you will choose one person who needs you.")
#         elif 'submit_lonelyhuman' in request.POST:
#             form = forms.LonelyHumanRegistrationForm(request.POST)
#             role = Role.LONELYHUMAN
#             success_message = _("Good job, now you have to give us additional information about your requirements with who and how you want to communicate with our volunteers")
        
#         if form.is_valid():
#             user = form.save()
#             user.role = role
#             user.save()
#             messages.success(request, success_message)
#             return redirect('login')
#     else:
#         form_volunteer = forms.VolunteerRegistrationForm()
#         form_lonelyhuman = forms.LonelyHumanRegistrationForm()

#     return render(request, 'register.html', {
#         'form_volunteer': form_volunteer,
#         'form_lonelyhuman': form_lonelyhuman
#     })


# def register(request:HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         role = request.POST.get('role')
#         if role =='lonelyhuman':
#             form = forms.LonelyHumanRegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 user.role = Role.LONELYHUMAN
#                 user.save()
#                 messages.success(request, _("Good job, now you have to give us additional information about your requirements with who and how you want to communicate with our volunteers"))
#                 return redirect('login')                  
#         elif role == 'Volunteer':
#             form = forms.LonelyHumanRegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 user.role = Role.VOLUNTEER
#                 user.save()
#                 messages.success(request, _("Thank you for your kindness! Now you can login and have to fill additional information and you will choose one person who needs you."))
#                 return redirect('login')
#     else:
#         form_volunteer = forms.VolunteerRegistrationForm()
#         form_lonelyhuman = forms.LonelyHumanRegistrationForm()
        
#     return render(request, 'register.html', {
#         'form_volunteer': form_volunteer,
#         'form_lonelyhuman': form_lonelyhuman
#     })



