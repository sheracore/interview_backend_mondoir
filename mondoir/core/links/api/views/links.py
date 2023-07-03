from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowStaffOrOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

from ..serializers import (
    LinkDetailSerializer,
    LinkSummarySerializer,
)
from ...models import Link
from ..filters import LinkFilterSet


class LinkViewSet(UserDataModelViewSet):
    queryset = Link.objects.none()
    filterset_class = LinkFilterSet
    model = Link
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'title',
       'description'
    )

    serializers = {
        'default': LinkSummarySerializer,
        'retrieve': LinkDetailSerializer,
        'create': LinkDetailSerializer,
        'update': LinkDetailSerializer,
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
        queryset = super(LinkViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
