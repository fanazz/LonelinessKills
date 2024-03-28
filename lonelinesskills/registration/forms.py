from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from . import models

class VolunteerUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''


class LonelyHumanUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = models.VolunteerProfile
        fields = ((_("age")), (_("gender")), (_("personal_no")), (_("phone")))

class LonelyHumanProfileForm(forms.ModelForm):
    class Meta:
        model = models.LonelyHumanProfile
        fields = ((_("age")), (_("gender")), (_("communication_style")), (_("phone")), (_("description")),
                (_("required_gender")), (_("required_age_from")), (_("required_age_to")))
        
      
# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
