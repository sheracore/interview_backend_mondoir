from mondoir.users.api.urls import user_api_urlpatterns
from mondoir.core.api.urls import core_api_urlpatterns
from mondoir.cvs.api.urls import cv_api_urlpatterns

mondoir_api_urlpatterns = (
    user_api_urlpatterns
    + core_api_urlpatterns
    + cv_api_urlpatterns
)
