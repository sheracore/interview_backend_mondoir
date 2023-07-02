from mondoir.cvs.models import Experience
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
from ..serializers import (
    ExperienceDetailSerializer,
    ExperienceSummarySerializer,
)
from ..filters import ExperienceFilterSet


class ExperienceViewSet(UserDataModelViewSet):
    queryset = Experience.objects.none()
    filterset_class = ExperienceFilterSet
    model = Experience
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'company_name',
       'position'
       'start_date',
       'end_date',
       'is_working_on_current_company'
    )

    serializers = {
        'default': ExperienceSummarySerializer,
        'retrieve': ExperienceDetailSerializer,
        'create': ExperienceDetailSerializer,
        'update': ExperienceDetailSerializer,
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
        queryset = super(ExperienceViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
