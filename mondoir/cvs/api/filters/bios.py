from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
    MultipleValueFilter
)


class BioFilterSet(UserDataModelFilterSet):
    content = filters.CharFilter(
        field_name='content',
        lookup_expr='icontains',
        help_text={'description': 'Title', "example": "backend"},
    )
    types = MultipleValueFilter(
        field_name='type',
        help_text={
            'description': 'Type of bio contents like email of phone number',
            "example": "POST->[1,2] queryparams->1,2,3"},
    )
