from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . import models



class LonelyHumanRegistrationForm(UserCreationForm):
    
    class Meta:
        model = models.LonelyHumanProfile
        fields = ('username', 'email')

   
class LonelyHumanProfileForm(forms.ModelForm):
    class Meta:
        model = models.LonelyHumanProfile
        fields = ['username', 'email', 'phone', 'age', 'gender', 'description', 'communication_style', 'required_age_from', 'required_age_to', 'required_gender']

class VolunteerRegistrationForm(UserCreationForm):
    
    class Meta:
        model = models.VolunteerProfile
        fields = ('username', 'email')

   
class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = models.VolunteerProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'identity_id', 'age', 'gender']