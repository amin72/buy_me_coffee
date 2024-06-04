from django.urls import path

from . import views


app_name = 'creator'

urlpatterns = [
    # creator page
    path(
        'page/',
        views.creator_page,
        name='creator_page'
    ),

    # creators
    path(
        'creators/',
        views.creators,
        name='creators'
    ),

    # creator
    path(
        'creator/<int:pk>/',
        views.creator,
        name='creator'
    ),

    # edit creator
    path(
        'creator/edit/',
        views.edit_creator,
        name='creator_edit'
    ),
]
