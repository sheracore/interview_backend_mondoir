import django_filters
from django_filters import rest_framework as filters

from mondoir.utilities.api.filters import (
    MultipleValueFilter,
    UserDataModelFilterSet,
)


class UserInformationFilterSet(UserDataModelFilterSet):
    first_name = filters.CharFilter(
        field_name='first_name',
        lookup_expr='icontains',
        help_text={'description': 'First name', "example": "mohammad"},
    )
    last_name = filters.CharFilter(
        field_name='last_name',
        lookup_expr='icontains',
        help_text={'description': 'Last name', "example": "ghafari"},
    )
    first_names = MultipleValueFilter(
        field_name='first_name',
        help_text={'description': 'First names', "example": "POST->['Mohammad', 'salar'] queryparams->sara,hasan"}
    )
    last_names = MultipleValueFilter(
        field_name='last_name',
        help_text={'description': 'Last names', "example": "POST->['Ghaffari', 'arabpour'] queryparams->ghaffari,arabpour"}
    )
    last_login = django_filters.DateTimeFromToRangeFilter(
        help_text={
            'description': 'Last login',
            "example": "last_login_after: '2022-12-28T15:33:57.7', last_login_before: '2023-12-28T15:33:57.7'",
        }
    )
    is_debug_mode = filters.BooleanFilter(
        field_name='is_debug_mode',
        help_text={'description': 'Is debug mode'},
    )
    email = filters.CharFilter(
        field_name='email',
        lookup_expr='icontains',
        help_text={'description': 'Email', "example": "sheracore@gmail.com"},
    )
    gender = MultipleValueFilter(
        field_name='gender',
        help_text={'description': 'gender', "example": "POST->[0,1,2] queryparams->0,1,2,3"},
    )
    languages = MultipleValueFilter(
        field_name='language',
        help_text={'description': 'language', "example": "POST->['en_US', 'en_GB'] queryparams->en_US,en_GB"},
    )
