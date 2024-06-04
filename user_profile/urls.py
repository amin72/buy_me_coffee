from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user_profile'

urlpatterns = [
    # login
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='user_profile/login.html'),
        name='login'
    ),
]
