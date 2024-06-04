from django.urls import path

from . import views


app_name = 'creator'

urlpatterns = [
    # creators
    path(
        'creators/',
        views.creators,
        name='creators'
    ),
]
