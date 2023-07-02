from mondoir.utilities.api.serializers import (
    UserDataModelDetailSerializer,
    UserDataModelSummarySerializer,
)
from .skills import SkillDetailSerializer
from .experiences import ExperienceDetailSerializer
from .educations import EducationDetailSerializer
from .certificates import CertificateDetailSerializer
from .bios import BioDetailSerializer
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
    bios = BioDetailSerializer(
        source='bio_cv',
        many=True,
        read_only=True,
    )
    skills = SkillDetailSerializer(
        source='skill_cv',
        many=True,
        read_only=True,
    )
    experiences = ExperienceDetailSerializer(
        source='experience_cv',
        many=True,
        read_only=True,
    )
    educations = EducationDetailSerializer(
        source='education_cv',
        many=True,
        read_only=True,
    )
    certificates = CertificateDetailSerializer(
        source='certificate_cv',
        many=True,
        read_only=True,
    )


    class Meta:
        model = CV
        fields = UserDataModelDetailSerializer.Meta.fields + CVSummarySerializer.Meta.fields + [
            'bios',
            'skills',
            'experiences',
            'educations',
            'certificates'
        ]

        read_only_fields = (
            UserDataModelDetailSerializer.Meta.read_only_fields
            + CVSummarySerializer.Meta.read_only_fields
            + [
                'bios',
                'skills',
                'experiences',
                'educations',
                'certificates'
            ]
        )

