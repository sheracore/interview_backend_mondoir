from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from mondoir.cvs.models import Experience, CV
from mondoir.utilities.permissions import IsSuperUserAccessPermission, AllowStaffOrOwner
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

    # TODO: should insert two below functions into the inherited class maby named CVVIEWSET
    def get_queryset(self):
        user = self.request.user
        queryset = super(ExperienceViewSet, self).get_queryset()
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
