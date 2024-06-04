from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    # core
    path("", include('core.urls')),

    # user_profile
    path("auth/", include('user_profile.urls')),
]
