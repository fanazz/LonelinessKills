from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from datetime import datetime

class LonelyHumanProfile(models.Model):
    AGES = (
        ('under18', _("Under 18")),
        ('18to25', '18 - 25'),
        ('26to35', '26 - 35'),
        ('36to50', '36 - 50'),
        ('over50', _("Over 50"))
    )

    GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('S', _("I do not want to say"))
    )

    REQUIRED_GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('B', _("Doesn't matter"))
    )

    COMMUNICATION = (
        ('E', _("By E-Mail")),
        ('P', _("By Phone")),
        ('L', _("Live meet"))
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(_("age"), max_length = 7, choices = AGES)
    gender = models.CharField(_("gender"), max_length = 1, choices = GENDERS)
    description = models.TextField(_("description"), max_length = 1000)
    communication_style = models.CharField(_("communication style"), max_length=1, choices = COMMUNICATION)
    required_age_from = models.IntegerField(_("required age from"))
    required_age_to = models.IntegerField(_("required age to"))
    required_gender = models.CharField(_("required gender"), max_length=1, choices = REQUIRED_GENDERS)
    

    class Meta:
        verbose_name = _("lonelyhumanprofile")
        verbose_name_plural = _("lonelyhumanprofiles")
        ordering = ['id']

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("lonelyhumanprofile_detail", kwargs={"pk": self.pk})
    

class VolunteerProfile(models.Model):
    GENDER_FOR_VOLUNTEER = (
        ('M', _("Male")),
        ('F', _("Female")),
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.IntegerField(_("age"))
    gender = models.CharField(_("gender"), max_length = 1, choices = GENDER_FOR_VOLUNTEER)
    personal_no = models.CharField(_("personal_no"), max_length = 15)
    lonelyhuman = models.ForeignKey(
        LonelyHumanProfile,
        verbose_name=_("volunteer"),
        on_delete=models.CASCADE, 
        related_name='lonelyhuman',
        null=True  
    )

    def save(self, *args, **kwargs):
        if not self.validate_personal_no():
            raise ValidationError('You are not real person!')
        if self.age != self.calculate_age_from_personal_no():
            raise ValidationError('You are not real person!') 
        super().save(*args, **kwargs)

    def validate_personal_no(self):
        personal_no = self.personal_no
        if len(personal_no) != 11:
            return False
        if not personal_no.isdigit():
            return False
        if (self.personal_no[0] == '3' or self.personal_no[0] == '5') and self.gender != 'M':
            return False
        if (self.personal_no[0] == '4' or self.personal_no[0] == '6') and self.gender != 'F':
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

    def calculate_age_from_personal_no(self):
        personal_no = self.personal_no
        birth_year = int(personal_no[1:3])
        today = datetime.now()
        return today.year - birth_year - ((today.month, today.day) < (int(personal_no[3:5]), int(personal_no[5:7])))

    class Meta:
        verbose_name = _("volunteerprofile")
        verbose_name_plural = _("volunteerprofiles")
        ordering = ['id']

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})    