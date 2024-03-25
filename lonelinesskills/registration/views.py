from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import models
from . import forms

User = get_user_model()

def register_as_volunteer(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form_user = forms.VolunteerUserForm(request.POST)
        form_profile = forms.VolunteerProfileForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid() and validate_personal_no(form_profile.instance.personal_no, form_profile.instance.gender) and calculate_age_from_personal_no():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, _("Thank you for your kindness! Now you can login and have to fill additional information and you will choose one person who needs you."))
            return redirect('login')
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
            messages.success(request, _("Good job, now you have to give us additional information about your requirements with who and how you want to comunnicate with our volunteers"))
            return redirect('login')  
    else:
        form_user = forms.LonelyHumanUserForm()
        form_profile = forms.LonelyHumanProfileForm()
    return render(request, 'register.html', {
        'title': _("Registration for Lonely"),
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
    personal_no = self.personal_no
    birth_year = int(personal_no[1:3])
    today = datetime.now()
    return today.year - birth_year - ((today.month, today.day) < (int(personal_no[3:5]), int(personal_no[5:7])))


@login_required
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    return render(request, 'registration/user_detail.html', {
        'object': user,
    })


# @login_required
# def volunteer_additional_information(request: HttpRequest) -> HttpResponse:
#     if  request.method == "POST":
#         form_user = forms.VolunteerRegistrationForm(request.POST, instance=request.user)
#         form_profile = forms.VolunteerProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form_user.is_valid() and form_profile.is_valid():
#             form_user.save()
#             form_profile.save()
#             messages.success(request, _("profile edited successfully").capitalize())
#             return redirect('user_detail_current')
#     else:
#         form_user = forms.VolunteerRegistrationForm(instance=request.user)
#         form_profile = forms.VolunteerProfileForm(instance=request.user.profile)
#     return render(request, 'user_profile/user_update.html', {
#         'form_user': form_user,
#         'form_profile': form_profile,
#     })


# @login_required
# def lonely_human_additional_information(request: HttpRequest) -> HttpResponse:
#     if  request.method == "POST":
#         form_user = forms.LonelyHumanUserForm(request.POST, instance=request.user)
#         form_profile = forms.LonelyHumanProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form_user.is_valid() and form_profile.is_valid():
#             form_user.save()
#             form_profile.save()
#             messages.success(request, _("profile edited successfully").capitalize())
#             return redirect('user_detail_current')
#     else:
#         form_user = forms.VolunteerRegistrationForm(instance=request.user)
#         form_profile = forms.VolunteerProfileForm(instance=request.user.profile)
#     return render(request, 'user_profile/user_update.html', {
#         'form_user': form_user,
#         'form_profile': form_profile,
#     })


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



# def create_volunteer(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form_user = forms.CreateUserForm(request.POST)
#         form_profile = forms.VolunteerProfileForm
#         if form_user.is_valid() and form_profile.is_valid():
#             user = form_user.save()
#             profile = form_profile.save(commit=False)
#             profile.user = user
#             profile.save()
#     else:
#         form_user = forms.CreateUserForm()
#         form_profile = forms.VolunteerProfileForm()

#     return render(request, 'register.html', {
#         'form_user': form_user,
#         'form_profile': form_profile
#     })

# def create_lonelyhuman(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form_user = forms.CreateUserForm(request.POST)
#         form_profile = forms.LonelyHumanProfileForm

#         # if form_user.is_valid() and form_profile.is_valid():
#         user = form_user.save()
#         profile = form_profile.save(commit=False)
#         profile.user = user
#         profile.save()
#     else:
#         form_user = forms.CreateUserForm()
#         form_profile = forms.LonelyHumanProfileForm()

#     return render(request, 'register.html', {
#         'form_user': form_user,
#         'form_profile': form_profile
#     })

# @login_required
# def choose_profile_type(request:HttpRequest) ->HttpResponse:
#     if request.method == "POST":
#         profile_type = request.POST.get("profile_type")
#         if profile_type == "lonelyhuman":
#             return redirect('create_lonelyhuman_profile')
#         elif profile_type == "volunteer":
#             return redirect('create_volunteer_profile')
#     return render(request, 'choose_profile_type.html')

# @login_required
# def create_lonely_human_profile(request:HttpRequest) ->HttpResponse:
#     if request.method == "POST":
#         lonely_human_profile_form = LonelyHumanProfileForm(request.POST)
#         if lonely_human_profile_form.is_valid():
#             instance = lonely_human_profile_form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             messages.success(request, _("Good job, we get your information and then will appear volunteer who matches your requirements it will contact with you as soon as posible."))
#             return redirect('home')
#     else:
#         lonely_human_profile_form = LonelyHumanProfileForm()
                    
#     context = {
#         'page_ref': 'create_lonelyhuman_profile',
#         'profile_form': lonely_human_profile_form,
#     }
#     return render(request, 'create_profile.html', context)

# @login_required
# def create_volunteer_profile(request:HttpRequest) ->HttpResponse:
#     if request.method == "POST":
#         volunteer_profile_form = VolunteerProfileForm(request.POST)
#         if volunteer_profile_form.is_valid():
#             instance = volunteer_profile_form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             messages.success(request, _("Thank you for your kindness! Now you you have to choose one person he needs you."))
#             return redirect('home')
#     else:
#         volunteer_profile_form = VolunteerProfileForm()
                    
#     context = {
#         'page_ref': 'create_volunteer_profile',
#         'profile_form': volunteer_profile_form,
#     }
#     return render(request, 'create_profile.html', context)