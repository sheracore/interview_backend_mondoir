from mondoir.cvs.models import CV
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowStaffOrOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
from ..serializers import (
    CVDetailSerializer,
    CVSummarySerializer,
)
from ..filters import CVFilterSet


class CVViewSet(UserDataModelViewSet):
    queryset = CV.objects.none()
    filterset_class = CVFilterSet
    model = CV
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'title',
    )

    serializers = {
        'default': CVSummarySerializer,
        'retrieve': CVDetailSerializer,
        'create': CVDetailSerializer,
        'update': CVDetailSerializer,
        'admin': CVSummarySerializer,
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

    def get_queryset(self):
        user = self.request.user
        queryset = super(CVViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
