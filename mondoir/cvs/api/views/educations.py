from mondoir.cvs.models import Education
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
from ..serializers import (
    EducationDetailSerializer,
    EducationSummarySerializer,
)
from ..filters import EducationFilterSet


class EducationViewSet(UserDataModelViewSet):
    queryset = Education.objects.none()
    filterset_class = EducationFilterSet
    model = Education
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'institution_name',
       'degree'
       'graduated_date'
    )

    serializers = {
        'default': EducationSummarySerializer,
        'retrieve': EducationDetailSerializer,
        'create': EducationDetailSerializer,
        'update': EducationDetailSerializer,
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
        queryset = super(EducationViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
