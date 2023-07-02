# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet
)


"""
Skill Model
"""


class ProficiencyType(models.IntegerChoices):
    FAMILIAR = 1, _('Familiar')
    BEGINNER = 2, _('Beginner')
    INTERMEDIATE = 3, _('Intermediate')
    ADVANCED = 4, _('Advanced')


class SkillQuerySet(UserDataModelQuerySet):
    pass


class SkillManager(UserDataModelManager):
    def get_queryset(self):
        return SkillQuerySet(self.model, using=self._db)


class Skill(UserDataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='skill_cv', verbose_name=_('CV'))
    title = models.CharField(max_length=50, verbose_name=_('Content'))
    proficiency = models.IntegerField(
        choices=ProficiencyType.choices,
        default=ProficiencyType.INTERMEDIATE,
        verbose_name=_('Proficiency'),
    )

    objects = SkillManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.title)

    class Meta:
        verbose_name = _('Skill model')
        verbose_name_plural = _('Skills')
