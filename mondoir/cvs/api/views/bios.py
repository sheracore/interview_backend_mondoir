from mondoir.cvs.models import Bio
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
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
        queryset = super(BioViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
