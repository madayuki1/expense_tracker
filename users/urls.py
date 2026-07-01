from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_view

urlpatterns = [
    path("register/", users_view.RegisterView.as_view(), name="register"),
]