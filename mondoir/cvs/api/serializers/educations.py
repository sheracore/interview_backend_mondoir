from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)

from ...models import Education

"""
Education
"""


class EducationSummarySerializer(UserDataModelSummarySerializer):

    class Meta:
        model = Education
        fields = UserDataModelSummarySerializer.Meta.fields + [
            'cv',
            'institution_name',
            'degree',
            'graduated_date'
        ]

        read_only_fields = UserDataModelSummarySerializer.Meta.read_only_fields + [
        ]


class EducationDetailSerializer(EducationSummarySerializer, UserDataModelDetailSerializer):
    class Meta:
        model = Education
        fields = UserDataModelDetailSerializer.Meta.fields + EducationSummarySerializer.Meta.fields + [
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + EducationSummarySerializer.Meta.read_only_fields
            + []
        )
