from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
)


class CVFilterSet(UserDataModelFilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        help_text={'description': 'Title', "example": "backend"},
    )
