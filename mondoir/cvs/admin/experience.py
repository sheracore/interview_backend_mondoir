# -*- coding: utf-8 -*-
from django.contrib import admin

from mondoir.cvs.models import Experience
from mondoir.utilities.admin import UserDataModelAdmin


class ExperienceAdmin(UserDataModelAdmin):
    fields = [
        'cv',
        'company_name',
        'position',
        'start_date',
        'end_date',
        'description',
        'is_working_on_current_company'
    ]
    list_display = [
        'cv',
        'company_name',
        'position',
        'start_date',
        'end_date',
        'is_working_on_current_company'
    ]
    list_filter = [
        'position',
        'is_working_on_current_company',
        'start_date',
        'end_date',
    ]
    search_fields = [
        'company_name',
        'position',
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
        Klass = ExperienceAdmin
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


admin.site.register(Experience, ExperienceAdmin)
