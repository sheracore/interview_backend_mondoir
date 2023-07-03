from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
    MultipleValueFilter
)


class LinkFilterSet(UserDataModelFilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        help_text={'description': 'Title', "example": "company link"},
    )
    description = MultipleValueFilter(
        field_name='description',
        lookup_expr='icontains',
        help_text={'description': 'description', "example": "upper intermediate"},
    )
