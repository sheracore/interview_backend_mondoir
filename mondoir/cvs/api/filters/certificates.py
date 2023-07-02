from django_filters import rest_framework as filters
from mondoir.utilities.api.filters import (
    UserDataModelFilterSet,
)


class CertificateFilterSet(UserDataModelFilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        help_text={'description': 'Name of your certificate', "example": "CCNA"},
    )
    issuer = filters.CharFilter(
        field_name='issuer',
        lookup_expr='icontains',
        help_text={'description': 'Name of your issuer', "example": "IBM"},
    )
    issuer_date = filters.DateFromToRangeFilter(
        field_name='issuer_date',
        help_text={
            'description': 'Issuer date',
            "example": "issuer_date_after: '2022-12-28', issuer_date_before: '2023-12-28'",
        },
    )
