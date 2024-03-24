from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from . import models

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''    

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

   
class LonelyHumanProfileForm(forms.ModelForm):
    age = (
    ('under18', _("Under 18")),
    ('18to25', '18 - 25'),
    ('26to35', '26 - 35'),
    ('36to50', '36 - 50'),
    ('over50', _("Over 50"))
    )

    gender = (
    ('male', _("Male")),
    ('female', _("Female")),
    ('secret', _("I do not want to say"))
    )

    required_gender = (
    ('male', _("Male")),
    ('female', _("Female")),
    ('both', _("Not important"))
    )

    communication = (
    ('email', _("By E-Mail")),
    ('phone', _("By Phone")),
    ('live', _("Live meet"))
    )

    phone = forms.CharField(label=_("phone"), max_length=50, required=False)
    age  = forms.ChoiceField(label=_("age"), choices=age, initial='', widget=forms.Select(), required=True)
    gender = forms.ChoiceField(label=_("gender"), choices=gender, initial='', widget=forms.Select(), required=True)
    description = forms.CharField(label=_("description"), widget=forms.Textarea(attrs={'class': 'description-field', 'maxlength': '1000'}), required=True)
    communication_style = forms.ChoiceField(label=_("communication style"), choices=communication, initial='', widget=forms.Select(), required=True)
    required_age_from = forms.IntegerField(label=_("required age from"), required=True, widget=forms.NumberInput(attrs={'min': 10, 'max': 120}))
    required_age_to = forms.IntegerField(label=_("required age to"), required=True, widget=forms.NumberInput(attrs={'min': 10, 'max': 120}))
    required_gender = forms.ChoiceField(label=_("required gender"), choices=required_gender,initial='', widget=forms.Select(), required=True)

    class Meta:
        model = models.LonelyHumanProfile
        fields = ['phone', 'age', 'gender', 'description', 'communication_style', 'required_age_from', 'required_age_to', 'required_gender']

   
class VolunteerProfileForm(forms.ModelForm):
    gender_for_volunteer = (
    ('male', _("Male")),
    ('female', _("Female")),
    )

    first_name = forms.CharField(label=_("first name"), max_length=30, required=True)
    last_name = forms.CharField(label=_("last name"), max_length=30, required=True)
    phone = forms.CharField(label=_("phone"), max_length=50, required=False)
    age = forms.CharField(label=_("Age"), max_length = 10, required=True)
    gender = forms.ChoiceField(label=_("gender"),choices=gender_for_volunteer, initial='', widget=forms.Select(), required=True)
    identity_id = forms.CharField(label=_("identity_id"), max_length=15, required=True)

    class Meta:
        model = models.VolunteerProfile
        fields = ['first_name', 'last_name', 'phone', 'identity_id', 'age', 'gender']

