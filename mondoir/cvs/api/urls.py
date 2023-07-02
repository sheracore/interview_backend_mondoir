from rest_framework import routers
from ..api.views import (
    CVViewSet,
    BioViewSet,
    CertificateViewSet,
    EducationViewSet,
    ExperienceViewSet,
    SkillViewSet
)

router = routers.DefaultRouter()
router.register(r'cvs', CVViewSet)
router.register(r'bios', BioViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'skills', SkillViewSet)

cv_api_urlpatterns = router.urls
