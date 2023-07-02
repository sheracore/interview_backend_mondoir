from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from mondoir.cvs.models import Bio, CV
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowStaffOrOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

from ..serializers import (
    BioDetailSerializer,
    BioSummarySerializer,
)
from ..filters import BioFilterSet


class BioViewSet(UserDataModelViewSet):
    queryset = Bio.objects.none()
    filterset_class = BioFilterSet
    model = Bio
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'type',
       'content'
    )

    serializers = {
        'default': BioSummarySerializer,
        'retrieve': BioDetailSerializer,
        'create': BioDetailSerializer,
        'update': BioDetailSerializer,
    }
    permission_classes_by_action = {
        'default': [
            IsSuperUserAccessPermission,
        ],
        'list': [
            AllowStaffOrOwner,
        ],
        'retrieve': [
            AllowStaffOrOwner,
        ],
        'update': [
            AllowStaffOrOwner,
        ],
        'create': [
            AllowStaffOrOwner,
        ],
        'destroy': [
            AllowStaffOrOwner,
        ],
    }

    # TODO: should insert two below functino into the inherited class maby named CVVIEWSET
    def get_queryset(self):
        user = self.request.user
        queryset = super(BioViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer, *args, **kwargs):
        user = self.get_user_perform_create()
        kwargs['user_id'] = user.pk
        data = self.request.data
        if cv := data.get('cv'):
            if not CV.objects.filter(pk=cv, user=user).exists():
                raise ValidationError({
                    "cv": [_("this cv does not belong to you")]
                })
        super(UserDataModelViewSet, self).perform_create(serializer=serializer, **kwargs)
