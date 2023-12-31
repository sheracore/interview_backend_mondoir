# -*- coding: utf-8 -*-

"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add generate_build_app_objs URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add generate_build_app_objs URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLConf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add generate_build_app_objs URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.utils.translation import gettext_lazy as _

from mondoir.urls import mondoir_urlpatterns

from .api import api_url

admin.autodiscover()

admin.site.site_title = _('Admin panel')
admin.site.site_header = _('Admin panel')


def index(request, *args, **kwargs):
    return HttpResponse("<h1>mondoir</h1>")


urlpatterns = mondoir_urlpatterns + [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(api_url)),
    # path('accounts/', include('allauth.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
