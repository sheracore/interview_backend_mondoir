# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db.models import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet
)
# from rest_framework.exceptions import ValidationError
from django.core.validators import ValidationError


"""
Experience Model
"""


class PositionType(models.IntegerChoices):
    SOFTWARE_ENGINEER = 1, _('Software Engineer')
    DATA_SCIENTIST = 2, _('Data Scientist')
    PRODUCT_MANAGER = 3, _('Product Manager')
    UX_UI_DESIGNER = 4, _('UX/UI Designer')
    DEVOPS_ENGINEER = 5, _('DevOps Engineer')
    QA_ENGINEER = 6, _('Quality Assurance Engineer')
    SYSTEMS_ADMINISTRATOR = 7, _('Systems Administrator')
    DATA_ENGINEER = 8, _('Data Engineer')
    SECURITY_ANALYST = 9, _('Security Analyst')
    TECHNICAL_SUPPORT_SPECIALIST = 10, _('Technical Support Specialist')
    PROJECT_MANAGER = 11, _('Project Manager')
    SALES_ENGINEER = 12, _('Sales Engineer')


class ExperienceQuerySet(UserDataModelQuerySet):
    pass


class ExperienceManager(UserDataModelManager):
    def get_queryset(self):
        return ExperienceQuerySet(self.model, using=self._db)


class Experience(UserDataModel):
    cv = models.ForeignKey('cvs.CV', on_delete=models.CASCADE, related_name='experience_cv', verbose_name=_('CV'))
    company_name = models.CharField(max_length=50, verbose_name=_('Company Name'))
    position = models.IntegerField(
        choices=PositionType.choices,
        default=PositionType.SOFTWARE_ENGINEER,
        verbose_name=_('Proficiency'),
    )
    start_date = models.DateField(null=False, blank=False, verbose_name=_('Start Date'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('End Date'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    is_working_on_current_company = models.BooleanField(default=False)

    objects = ExperienceManager()

    def __str__(self):
        return "%s - %s" % (self.pk, self.company_name)

    class Meta:
        verbose_name = _('Experience model')
        verbose_name_plural = _('Experiences')

    def clean(self):
        if self.end_date and self.is_working_on_current_company:
            raise ValidationError({
                'end_date': [_("Can't fill is_working_on_current_company and end_date together")]
            })
