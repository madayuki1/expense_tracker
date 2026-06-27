from django.shortcuts import render
from .models import Account, Transaction, Category
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django import forms
from django.urls import reverse_lazy


# Create your views here.
class AccountForm(forms.ModelForm):
    """Form definition for Account."""

    class Meta:
        """Meta definition for Accountform."""

        model = Account
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name-id",
                    "placeholder": "Account Name"
                }
            ),
            "balance": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "balance-id",
                    "placeholder": "Account Balance"
                }
            ),
        }


class AccountListView(ListView):
    model = Account
    template_name = "finances/account_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset # TODO
        return queryset 


class AccountCreateView(CreateView):
    model = Account
    template_name = "finances/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy('account_list')


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy("account_list")


class AccountUpdateView(UpdateView):
    model = Account
    template_name = "finances/account_update.html"
    form_class = AccountForm
    success_url = reverse_lazy('account_list')


class TransactionListView(ListView):
    model = Transaction
    template_name = "finances/transaction_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset # TODO
        return queryset 


class CategoryListView(ListView):
    model = Category
    template_name = "finances/category_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset # TODO
        return queryset