from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from registration.models import *


class VolunteerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'age', 'gender']
    # list_display_links = ['username']
    # list_filter = ['username', 'age', 'gender']
    # search_fields = ['username', 'gender']
    # readonly_fields = ['username', 'age', 'gender']
    # fieldsets = (
    #     (_("general").title(), {
    #         "fields": (
    #             'username', 'first_name', 'last_name'
    #         ),
    #     }),
    #     (_("comunication").title(), {
    #         "fields": (
    #             ('phone', 'email'),
    #         ),
    #     }),
    #     (_("information").title(), {
    #         "fields": (
    #             ('age', 'gender'),
    #         ),
    #     }),
    # )

class LonelyHumanProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'description', 'communication_style', 'required_age_from', 'required_age_to', 'required_gender']
    # list_display_links = ['username']
    # list_filter = ['communication_style', 'required_age_from', 'required_age_to', 'required_gender']
    # search_fields = ['description', 'gender']
    # fieldsets = (
    #     (_("general").title(), {
    #         "fields": (
    #             'username', 'age', 'gender'
    #         ),
    #     }),
    #     (_("comunication").title(), {
    #         "fields": (
    #             ('phone', 'email'),
    #         ),
    #     }),
    #     (_("Looking for").title(), {
    #         "fields": (
    #             ('required_age_from', 'required_age_to', 'required_gender', 'communication_style'),
    #             'description'
    #         ),
    #     }),
    # )


admin.site.register(VolunteerProfile, VolunteerProfileAdmin)
admin.site.register(LonelyHumanProfile, LonelyHumanProfileAdmin)