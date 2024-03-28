from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_board'
    verbose_name = _('main_board')
