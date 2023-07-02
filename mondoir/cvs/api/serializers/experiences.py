from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Experience

"""
Experience
"""


class ExperienceSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Experience
        fields = UserDataModelSummarySerializer.Meta.fields + [
            "cv",
            'company_name',
            'position',
            'start_date',
            'end_date',
            'description',
            'is_working_on_current_company'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class ExperienceDetailSerializer(ExperienceSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Experience
        fields = UserDataModelDetailSerializer.Meta.fields + ExperienceSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + ExperienceSummarySerializer.Meta.read_only_fields
            + []
        )
