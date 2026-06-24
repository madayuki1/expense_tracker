from django.shortcuts import render
from .models import Account, Transaction, Category
from django.views.generic import ListView

# Create your views here.

class AccountListView(ListView):
    model = Account
    template_name = "account_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset # TODO
        return queryset 


class TransactionListView(ListView):
    model = Transaction
    template_name = "transaction_list.html"


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
