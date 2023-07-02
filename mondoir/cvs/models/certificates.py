# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet
)

"""
Certificate Model
"""


class CertificateQuerySet(UserDataModelQuerySet):
    pass


class CertificateManager(UserDataModelManager):
    def get_queryset(self):
        return CertificateQuerySet(self.model, using=self._db)


class Certificate(UserDataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='certificate_cv', verbose_name=_('CV'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    issuer = models.CharField(max_length=100, verbose_name=_('Issuer'))
    issuer_date = models.DateField(null=True, blank=True, verbose_name=_('Issuer Date'))

    objects = CertificateManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.name)

    class Meta:
        verbose_name = _('Certificate model')
        verbose_name_plural = _('Certificates')
