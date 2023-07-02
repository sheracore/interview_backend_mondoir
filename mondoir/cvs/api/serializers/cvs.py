from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import CV

"""
CV
"""


class CVSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = CV
        fields = UserDataModelSummarySerializer.Meta.fields + [
            'title'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [

        ]


class CVDetailSerializer(CVSummarySerializer, UserDataModelDetailSerializer):
    # bios = AnswerOptionDetailSerializer(
    #     source='answeroption_set',
    #     many=True,
    #     read_only=True,
    # )

    class Meta:
        model = CV
        fields = UserDataModelDetailSerializer.Meta.fields + CVSummarySerializer.Meta.fields + [
            # 'bios'
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + CVSummarySerializer.Meta.read_only_fields
            + [
            # 'bios'
            ]
        )

