from mondoir.cvs.models import Certificate
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowOwner
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
            AllowOwner,
        ],
        'retrieve': [
            AllowOwner,
        ],
        'update': [
            AllowOwner,
        ],
        'create': [
            AllowOwner,
        ],
        'destroy': [
            AllowOwner,
        ],
    }

    def get_queryset(self):
        user = self.request.user
        queryset = super(CertificateViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
