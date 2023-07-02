# -*- coding: utf-8 -*-
from django.contrib import admin

from mondoir.cvs.models import Bio
from mondoir.utilities.admin import UserDataModelAdmin


class BioAdmin(UserDataModelAdmin):
    fields = [
        'cv',
        'type',
        'content'
    ]
    list_display = [
        'cv',
        'type',
        'content'
    ]
    list_filter = [
        'type'
    ]
    search_fields = [
        'type',
        'content',
    ]
    exclude = []
    raw_id_fields = [
        'cv'
    ]
    readonly_fields = []
    allowed_actions = []
    inlines = []
    save_as = True

    def __init__(self, *args, **kwargs):
        Klass = BioAdmin
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


admin.site.register(Bio, BioAdmin)
