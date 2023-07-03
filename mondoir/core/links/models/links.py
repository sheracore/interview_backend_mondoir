# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from mondoir.utilities.db import (
    UserDataModel,
    UserDataModelManager,
    UserDataModelQuerySet,
)

"""
Link Model
"""


class LinkQuerySet(UserDataModelQuerySet):
    def __init__(self, *args, **kwargs):
        super(LinkQuerySet, self).__init__(*args, **kwargs)


class LinkManager(UserDataModelManager):
    def get_queryset(self):
        return LinkQuerySet(self.model, using=self._db)


class Link(UserDataModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    description = models.CharField(max_length=255, blank=True, verbose_name=_('Description'))
    url = models.URLField(
        verbose_name=_('URL'),
    )
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='link',
        verbose_name=_('Content Type'),
    )
    object_id = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name=_('Object ID'),
    )

    objects = LinkManager()

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return "%s - %s" % (self.pk, self.title)
