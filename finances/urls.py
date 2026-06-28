from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/", views.AccountListView.as_view(), name="account_list"),
    path("accounts/create", views.AccountCreateView.as_view(), name="account_create"),
    path("accounts/delete/<int:pk>", views.AccountDeleteView.as_view(), name="account_delete"),
    path("accounts/update/<int:pk>", views.AccountUpdateView.as_view(), name="account_update"),
    path("", views.TransactionListView.as_view(), name="transaction_list"),
    path("create", views.TransactionCreateView.as_view(), name="transaction_create"),
    path("delete/<int:pk>", views.TransactionDeleteView.as_view(), name="transaction_delete"),
    path("update/<int:pk>", views.TransactionUpdateView.as_view(), name="transaction_update"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/create", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/delete/<int:pk>", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("categories/update/<int:pk>", views.CategoryUpdateView.as_view(), name="category_update"),
]