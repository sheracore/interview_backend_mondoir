from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
    MultipleValueFilter
)


class EducationFilterSet(UserDataModelFilterSet):
    institution_name = filters.CharFilter(
        field_name='institution_name',
        lookup_expr='icontains',
        help_text={'description': 'Institution name', "example": "k.n toosi"},
    )
    degree = MultipleValueFilter(
        field_name='degree',
        help_text={'description': 'Degree', "example": "POST->[1,2] queryparams->1,2,3"},
    )
    graduated_date = filters.DateFromToRangeFilter(
        field_name='graduated_date',
        help_text={
            'description': 'Graduated date',
            "example": "graduated_date_after: '2022-12-28', graduated_date_before: '2023-12-28'",
        },
    )
