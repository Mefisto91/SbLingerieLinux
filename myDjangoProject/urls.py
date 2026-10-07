from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("20sb91-gestion-sbl-colombia/", admin.site.urls),
    path("", include("myDjangoApp.urls", namespace="myDjangoApp")),
]

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]