# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    DataModel,
    DataModelManager,
    DataModelQuerySet
)
from ..utilities import validate_bio_content


"""
Bio Model
"""


class BioType(models.IntegerChoices):
    FULLNAME = 1, _('Fullname')
    EMAIL = 2, _('Email')
    PHONE = 3, _('Phone')
    DATEOFBIRTH = 4, _('Date of birth')
    AGE = 5, _('Age')
    WEBSITE = 6, _('Website')


class BioQuerySet(DataModelQuerySet):
    pass


class BioManager(DataModelManager):
    def get_queryset(self):
        return BioQuerySet(self.model, using=self._db)


class Bio(DataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='bio_cv', verbose_name=_('CV'))
    type = models.IntegerField(
        choices=BioType.choices,
        default=BioType.FULLNAME,
        verbose_name=_('Type'),
    )
    content = models.CharField(max_length=255, blank=True, verbose_name=_('Content'))

    objects = BioManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.type)

    class Meta:
        verbose_name = _('Bio model')
        verbose_name_plural = _('Bios')

    def clean(self):
        # TODO: validate_duplicate (just one bio for each type) while creating : if Bio.objects.filter(type=self.type).exists()
        validate_bio_content(BioType(self.type).name, self.content)
