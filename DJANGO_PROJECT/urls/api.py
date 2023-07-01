from rest_framework import routers

from mondoir.api.urls import mondoir_api_urlpatterns

router = routers.DefaultRouter()

api_url = router.urls
api_url = api_url + mondoir_api_urlpatterns
