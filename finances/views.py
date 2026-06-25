from django.shortcuts import render
from .models import Account, Transaction, Category
from django.views.generic import ListView, CreateView
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy


# Create your views here.
class BaseFormHelper:
    def setup_helper(self):
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))
        
class AccountForm(BaseFormHelper, forms.ModelForm):
    """Form definition for Account."""

    class Meta:
        """Meta definition for Accountform."""

        model = Account
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_helper()


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