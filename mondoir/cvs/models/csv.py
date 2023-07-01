# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet
)


"""
CV Model
"""


class CVQuerySet(UserDataModelQuerySet):
    pass


class CVManager(UserDataModelManager):
    def get_queryset(self):
        return CVQuerySet(self.model, using=self._db)


class CV(UserDataModel):
    title = models.CharField(
        max_length=50,
        verbose_name=_('Title'),
    )
    url = models.URLField(
        verbose_name=_('URL'),
    )

    objects = CVManager()

    class Meta:
        app_label = 'cvs'
        verbose_name = _('CV model')
        verbose_name_plural = _('CVs')

    def __str__(self):
        return "%s - %s" % (self.pk, self.title)
