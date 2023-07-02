from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from mondoir.cvs.models import Certificate, CV
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowStaffOrOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
from ..serializers import (
    CertificateDetailSerializer,
    CertificateSummarySerializer,
)
from ..filters import CertificateFilterSet


class CertificateViewSet(UserDataModelViewSet):
    queryset = Certificate.objects.none()
    filterset_class = CertificateFilterSet
    model = Certificate
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'name',
       'issuer',
       'issuer_date'
    )

    serializers = {
        'default': CertificateSummarySerializer,
        'retrieve': CertificateDetailSerializer,
        'create': CertificateDetailSerializer,
        'update': CertificateDetailSerializer,
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
        queryset = super(CertificateViewSet, self).get_queryset()
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
