from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
    MultipleValueFilter
)


class SkillFilterSet(UserDataModelFilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        help_text={'description': 'title', "example": "django"},
    )
    proficiencies = MultipleValueFilter(
        field_name='proficiency',
        help_text={'description': 'proficiency', "example": "POST->[1,2] queryparams->1,2,3"},
    )
