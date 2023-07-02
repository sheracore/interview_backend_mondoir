# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet
)

"""
Education Model
"""


class DegreeLevel(models.IntegerChoices):
    ASSOCIATE = 1, _('Associate')
    CERTIFICATE = 2, _('Certificate')
    DIPLOMA = 3, _('Diploma')
    BACHELOR = 4, _('Bachelor')
    MASTER = 5, _('Master')
    DOCTORATE = 6, _('Doctorate')
    OTHER = 7, _('Other')


class EducationQuerySet(UserDataModelQuerySet):
    pass


class EducationManager(UserDataModelManager):
    def get_queryset(self):
        return EducationQuerySet(self.model, using=self._db)


class Education(UserDataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='education_cv', verbose_name=_('CV'))
    institution_name = models.CharField(max_length=50, verbose_name=_('Institution Name'))
    degree = models.IntegerField(
        choices=DegreeLevel.choices,
        default=DegreeLevel.BACHELOR,
        verbose_name=_('Degree'),
    )
    graduated_date = models.DateField(null=True, blank=True, verbose_name=_('Graduated date'))

    objects = EducationManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.institution_name)

    class Meta:
        verbose_name = _('Education model')
        verbose_name_plural = _('Educations')
