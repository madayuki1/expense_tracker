from django.shortcuts import render, redirect
from .models import Account, Transaction, Category
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
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
                    "placeholder": "Account Name",
                }
            ),
            "balance": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "balance-id",
                    "placeholder": "Account Balance",
                }
            ),
        }
    

class AccountListView(ListView):
    model = Account
    template_name = "finances/account_list.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            user = self.request.user.id
        )
        return queryset


class AccountDetailView(DetailView):
    model = Account
    template_name = "finances/account_detail.html"

class AccountCreateView(CreateView):
    model = Account
    template_name = "finances/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy("account_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy("account_list")


class AccountUpdateView(UpdateView):
    model = Account
    template_name = "finances/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy("account_list")


class TransactionListView(ListView):
    model = Transaction
    template_name = "finances/transaction_list.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset  # TODO
        return queryset


class TransactionForm(forms.ModelForm):
    """Form definition for Transaction."""

    class Meta:
        """Meta definition for Transactionform."""

        model = Transaction
        fields = "__all__"
        # account = forms.MultipleChoiceField(
        #     required=True
        # )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name-id",
                    "placeholder": "Transaction Name",
                }
            ),
            "account": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "amount-id",
                    "placeholder": "Transaction Amount",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "description-id",
                    "placeholder": "Transaction Description",
                }
            ),
        }

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = "finances/transaction_form.html"
    form_class = TransactionForm
    success_url = reverse_lazy("transaction_list")


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "finances/transaction_detail.html"


class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = "finances/transaction_form.html"
    form_class = TransactionForm
    success_url = reverse_lazy("transaction_list")


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "finances/transaction_confirm_delete.html"
    success_url = reverse_lazy("transaction_list")


class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name-id",
                    "placeholder": "Category Name",
                }
            )
        }

class CategoryListView(ListView):
    model = Category
    template_name = "finances/category_list.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset  # TODO
        return queryset


class CategoryCreateView(CreateView):
    model = Category
    template_name = "finances/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "finances/category_detail.html"


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "finances/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")
