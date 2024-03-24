from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _


class LonelyHumanProfile(models.Model):
    ages = (
    ('under18', _("Under 18")),
    ('18to25', '18 - 25'),
    ('26to35', '26 - 35'),
    ('36to50', '36 - 50'),
    ('over50', _("Over 50"))
    )

    genders = (
    ('male', _("Male")),
    ('female', _("Female")),
    ('secret', _("I do not want to say"))
    )

    required_genders = (
    ('male', _("Male")),
    ('female', _("Female")),
    ('both', _("Not important"))
    )

    communication = (
    ('email', _("By E-Mail")),
    ('phone', _("By Phone")),
    ('live', _("Live meet"))
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    username = models.CharField(_("username"), max_length=20, db_index=True, unique=True)
    email = models.EmailField(_("email"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(_("Age"), max_length = 10, choices = ages)
    gender = models.CharField(_("gender"),max_length = 10, choices = genders)
    description = models.TextField(_("description"), max_length=1000)
    communication_style = models.CharField(_("communication Style"), max_length=10, choices = communication)
    required_age_from = models.IntegerField(_("required Age From"))
    required_age_to = models.IntegerField(_("required Age To"))
    required_gender = models.CharField(_("required Gender"), max_length=10, choices = required_genders)
    

    class Meta:
        verbose_name = _("lonelyhumanprofile")
        verbose_name_plural = _("lonelyhumanprofiles")
        ordering = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("lonelyhumanprofile_detail", kwargs={"pk": self.pk})
    

class VolunteerProfile(models.Model):
    gender_for_volunteer = (
    ('male', _("Male")),
    ('female', _("Female")),
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    username = models.CharField(_("user name"), max_length=20, db_index=True, unique=True)
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    email = models.CharField(_("email"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(_("Age"), max_length = 10)
    gender = models.CharField(_("gender"), max_length = 10, choices = gender_for_volunteer)
    identity_id = models.CharField(_("identity_id"), max_length = 15)
    lonelyhuman = models.ForeignKey(
        LonelyHumanProfile,
        verbose_name=_("volunteer"),
        on_delete=models.CASCADE, 
        related_name='lonelyhuman',
        null=True  
    )


    class Meta:
        verbose_name = _("volunteerprofile")
        verbose_name_plural = _("volunteerprofiles")
        ordering = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})    

    
    
