from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

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

gender_for_volunteer = (
    ('male', _("Male")),
    ('female', _("Female")),
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

class Volunteer(models.Model):
    username = models.CharField(_("user name"), max_length=20, db_index=True)
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    email = models.CharField(_("email"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10, choices = gender_for_volunteer)
    identity_id = models.CharField(max_length = 11, null=False, blank=False, default="456")
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("volunteers")
        ordering = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("volunteer_detail", kwargs={"pk": self.pk})


class LonelyHuman(models.Model):
    name = models.CharField(_("name"), max_length=30, db_index=True)
    email = models.CharField(_("email"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(max_length = 10, choices = ages)
    gender = models.CharField(max_length = 10, choices = genders)
    description = models.CharField(max_length=1000)
    communication_style = models.CharField(max_length=10, choices = communication)
    required_age_from = models.IntegerField()
    required_age_to = models.IntegerField()
    required_gender = models.CharField(max_length=10, choices = required_genders)
    volunteer = models.ForeignKey(
        Volunteer,
        verbose_name=_("volunteer"),
        on_delete=models.CASCADE, 
        related_name='lonelyhuman',
        null=True  
    )

    class Meta:
        verbose_name = _("lonelyhuman")
        verbose_name_plural = _("lonelyhumans")
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lonelyhuman_detail", kwargs={"pk": self.pk})