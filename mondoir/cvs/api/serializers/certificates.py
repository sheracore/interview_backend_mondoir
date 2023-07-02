from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Certificate

"""
Certificate
"""


class CertificateSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Certificate
        fields = UserDataModelSummarySerializer.Meta.fields + [
            'cv',
            'name',
            'issuer',
            'issuer_date'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class CertificateDetailSerializer(CertificateSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Certificate
        fields = UserDataModelDetailSerializer.Meta.fields + CertificateSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + CertificateSummarySerializer.Meta.read_only_fields
            + []
        )
