from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Bio

"""
Bio
"""


class BioSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Bio
        fields = UserDataModelSummarySerializer.Meta.fields + [
            'cv',
            'type',
            'content'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class BioDetailSerializer(BioSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Bio
        fields = UserDataModelDetailSerializer.Meta.fields + BioSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + BioSummarySerializer.Meta.read_only_fields
            + [
            ]
        )

