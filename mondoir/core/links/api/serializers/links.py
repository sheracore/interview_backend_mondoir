from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Link

"""
Link
"""


class LinkSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Link
        fields = UserDataModelSummarySerializer.Meta.fields + [
            'title',
            'description',
            'url'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class LinkDetailSerializer(LinkSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Link
        fields = UserDataModelDetailSerializer.Meta.fields + LinkSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + LinkSummarySerializer.Meta.read_only_fields
            + [
            ]
        )

