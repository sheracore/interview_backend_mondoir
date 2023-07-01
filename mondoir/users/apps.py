from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = 'mondoir.users'
    app_label = 'users'
    verbose_name = _('User')
    verbose_name_plural = _('Users')

