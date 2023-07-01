from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CVApp(AppConfig):
    name = 'mondoir.cvs'
    app_label = 'cvs'
    verbose_name = _('CV')
    verbose_name_plural = _('CVs')
