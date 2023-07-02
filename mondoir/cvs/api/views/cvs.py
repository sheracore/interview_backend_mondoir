from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from mondoir.cvs.models import CV
from mondoir.utilities.permissions import AllowStaff, IsSuperUserAccessPermission, AllowOwner
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
        'filter_admin': CVSummarySerializer,
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
            IsSuperUserAccessPermission,
        ],
    }

    def get_queryset(self):
        user = self.request.user
        queryset = super(CVViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
