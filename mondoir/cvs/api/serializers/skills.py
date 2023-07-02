from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Skill

"""
Skill
"""


class SkillSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Skill
        fields = UserDataModelSummarySerializer.Meta.fields + [
            "cv",
            'title',
            'proficiency'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class SkillDetailSerializer(SkillSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Skill
        fields = UserDataModelDetailSerializer.Meta.fields + SkillSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + SkillSummarySerializer.Meta.read_only_fields
            + []
        )
