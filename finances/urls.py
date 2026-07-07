from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("accounts/", views.AccountListView.as_view(), name="account_list"),
    path("accounts/create", views.AccountCreateView.as_view(), name="account_create"),
    path("accounts/detail/<int:pk>", views.AccountDetailView.as_view(), name="account_detail"),
    path("accounts/delete/<int:pk>", views.AccountDeleteView.as_view(), name="account_delete"),
    path("accounts/update/<int:pk>", views.AccountUpdateView.as_view(), name="account_update"),
    path("transactions/", views.TransactionListView.as_view(), name="transaction_list"),
    path("transactions/create", views.TransactionCreateView.as_view(), name="transaction_create"),
    path("transactions/detail/<int:pk>", views.TransactionDetailView.as_view(), name="transaction_detail"),
    path("transactions/delete/<int:pk>", views.TransactionDeleteView.as_view(), name="transaction_delete"),
    path("transactions/update/<int:pk>", views.TransactionUpdateView.as_view(), name="transaction_update"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/create", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/detail/<int:pk>", views.CategoryDetailView.as_view(), name="category_detail"),
    path("categories/delete/<int:pk>", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("categories/update/<int:pk>", views.CategoryUpdateView.as_view(), name="category_update"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]