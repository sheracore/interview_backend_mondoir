from mondoir.cvs.models import Skill
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowOwner
from mondoir.utilities.api.views import UserDataModelViewSet
from mondoir.utilities.api.paginations import StandardResultsSetPagination

# ViewSets define the view behavior.
from ..serializers import (
    SkillDetailSerializer,
    SkillSummarySerializer,
)
from ..filters import SkillFilterSet


class SkillViewSet(UserDataModelViewSet):
    queryset = Skill.objects.none()
    filterset_class = SkillFilterSet
    model = Skill
    pagination_class = StandardResultsSetPagination
    OrderingFilter = (
       'title',
       'proficiency'
    )

    serializers = {
        'default': SkillSummarySerializer,
        'retrieve': SkillDetailSerializer,
        'create': SkillDetailSerializer,
        'update': SkillDetailSerializer,
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
        queryset = super(SkillViewSet, self).get_queryset()
        if user.is_authenticated and self.action.find('admin') == -1:
            queryset = queryset.filter(user=user)
        return queryset
