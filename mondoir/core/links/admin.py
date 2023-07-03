# -*- coding: utf-8 -*-
from django.contrib import admin

from mondoir.core.links.models import Link
from mondoir.utilities.admin import UserDataModelAdmin


class LinkAdmin(UserDataModelAdmin):
    fields = [
        'title',
        'description',
        'url',
        'content_type',
        'object_id',
    ]
    list_display = [
        'title',
        'description',
        'url',
        'content_type',
        'object_id',
    ]
    list_filter = [
    ]
    search_fields = [
        'title',
        'description',
    ]
    exclude = []
    raw_id_fields = [
    ]
    readonly_fields = []
    allowed_actions = []
    inlines = []
    save_as = True

    def __init__(self, *args, **kwargs):
        Klass = LinkAdmin
        Klass_parent = UserDataModelAdmin

        super(Klass, self).__init__(*args, **kwargs)

        self.fields = Klass_parent.fields + self.fields
        self.list_display = Klass_parent.list_display + self.list_display
        self.list_filter = Klass_parent.list_filter + self.list_filter
        self.search_fields = Klass_parent.search_fields + self.search_fields
        self.exclude = Klass_parent.exclude + self.exclude
        self.raw_id_fields = Klass_parent.raw_id_fields + self.raw_id_fields
        self.readonly_fields = Klass_parent.readonly_fields + self.readonly_fields
        self.allowed_actions = Klass_parent.allowed_actions + self.allowed_actions
        self.inlines = Klass_parent.inlines + self.inlines


admin.site.register(Link, LinkAdmin)
