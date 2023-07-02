from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
    MultipleValueFilter
)


class ExperienceFilterSet(UserDataModelFilterSet):
    company_name = filters.CharFilter(
        field_name='company_name',
        lookup_expr='icontains',
        help_text={'description': 'company name', "example": "farafan"},
    )
    description = filters.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        help_text={'description': 'description', "example": "more than 5 years experiece"},
    )
    position = MultipleValueFilter(
        field_name='position',
        help_text={'description': 'position', "example": "POST->[0,1,2] queryparams->0,1,2,3"},
    )
    start_date = filters.DateFromToRangeFilter(
        field_name='start_date',
        help_text={
            'description': 'start date',
            "example": "start_date_after: '2022-12-28', start_date_before: '2023-12-28'",
        },
    )
    end_date = filters.DateFromToRangeFilter(
        field_name='end_date',
        help_text={
            'description': 'end date',
            "example": "end_date_after: '2022-12-28', end_date_before: '2023-12-28'",
        },
    )
    is_working_on_current_company = filters.BooleanFilter(
        field_name='is_working_on_current_company',
        help_text={'description': 'is working on current company'},
    )
