from rest_framework import serializers


from mondoir.users.models import UserInformation
from mondoir.utilities.api.serializers import (
    DataModelSummarySerializer,
    UserDataModelDetailSerializer,
)


class UserInformationSummarySerializer(DataModelSummarySerializer):

    class Meta:
        model = UserInformation
        fields = DataModelSummarySerializer.Meta.fields + [
            'email',
            'user_id',
            'first_name',
            'last_name',
        ]

        read_only_fields = DataModelSummarySerializer.Meta.read_only_fields + [
            'user_id',
        ]


class UserInformationAdminSummarySerializer(UserInformationSummarySerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = UserInformation
        fields = UserInformationSummarySerializer.Meta.fields + [
            'username',
            'last_login',
            'gender',
            'is_staff',
            'language',
            'timezone',
            'email',
        ]

        read_only_fields = UserInformationSummarySerializer.Meta.read_only_fields + [
            'last_login',
            'is_staff',
            'username'
        ]

    def get_username(self, obj):
        return str(obj.user.username)


class UserInformationDetailSerializer(UserDataModelDetailSerializer, UserInformationAdminSummarySerializer):
    class Meta:
        model = UserInformation
        fields = (
            UserInformationAdminSummarySerializer.Meta.fields
            + UserDataModelDetailSerializer.Meta.fields
            + []
        )

        read_only_fields = (
            UserInformationAdminSummarySerializer.Meta.read_only_fields
            + UserDataModelDetailSerializer.Meta.read_only_fields
            + []
        )
