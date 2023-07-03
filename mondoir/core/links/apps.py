from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinkConfig(AppConfig):
    name = 'mondoir.core.links'
    app_label = 'links'
    verbose_name = _('Link')
    verbose_name_plural = _('Cores')
