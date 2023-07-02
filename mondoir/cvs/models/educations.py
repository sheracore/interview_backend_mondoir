# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    DataModel,
    DataModelManager,
    DataModelQuerySet
)

"""
Education Model
"""


class DegreeLevel(models.IntegerChoices):
    MASTER = 1, _('Master')
    BACHELOR = 2, _('Bachelor')
    DOCTORATE = 3, _('Doctorate')
    ASSOCIATE = 4, _('Associate')
    DIPLOMA = 5, _('Diploma')
    CERTIFICATE = 6, _('Certificate')
    OTHER = 7, _('Other')


class EducationQuerySet(DataModelQuerySet):
    pass


class EducationManager(DataModelManager):
    def get_queryset(self):
        return EducationQuerySet(self.model, using=self._db)


class Education(DataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='education_cv', verbose_name=_('CV'))
    institution_name = models.CharField(max_length=50, verbose_name=_('Institution Name'))
    degree = models.IntegerField(
        choices=DegreeLevel.choices,
        default=DegreeLevel.BACHELOR,
        verbose_name=_('Degree'),
    )
    graduated_year = models.DateField(null=True, blank=True, verbose_name=_('Graduated Year'))

    objects = EducationManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.institution_name)

    class Meta:
        verbose_name = _('Education model')
        verbose_name_plural = _('Educations')
