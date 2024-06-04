from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),

    # core
    path("", include('core.urls')),

    # user_profile
    path("auth/", include('user_profile.urls')),

    # creator
    path("creator/", include('creator.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
