from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountListView.as_view(), name="account_list"),
    path("accounts/create", views.AccountCreateView.as_view(), name="account_create"),
    path("", views.TransactionListView.as_view(), name="transaction_list"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
]