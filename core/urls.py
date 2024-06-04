from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    # core
    path("", views.index, name='index'),
]
