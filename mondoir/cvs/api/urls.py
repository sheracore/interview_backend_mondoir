from rest_framework import routers
from ..api.views import CVViewSet

router = routers.DefaultRouter()
router.register(r'cvs', CVViewSet)

cv_api_urlpatterns = router.urls
