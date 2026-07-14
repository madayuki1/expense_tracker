from django.shortcuts import render, redirect
from .models import Account, Transaction, Category, Budget
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
import calendar
from django.db.models import Avg, Sum
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
class BudgetListView(ListView):
    model = Budget
    template_name = "finances/budget_list"

    def get_queryset(self):
        queryset = super(BudgetListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class BudgetForm(forms.ModelForm):
    """Form definition for Budget."""

    class Meta:
        """Meta definition for Budgetform."""

        model = Budget 
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name-id",
                    "placeholder": "Budget Name",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "type": forms.Select(attrs={"class": "form-select"}),
            "limit": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "amount-id",
                    "placeholder": "Budget Limit",
                }
            ),
        }

class BudgetCreateView(CreateView):
    model = Budget
    template_name = "finances/budget_form.html"
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = "finances/budget_form.html"
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BudgetDetailView(DetailView):
    model = Budget
    template_name = "finances/budget_detail.html"

class BudgetDeleteView(DeleteView):
    model = Budget
    success_url = reverse_lazy('budget_list')

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

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "finances/account_list.html"
    # paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = "finances/account_detail.html"

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "finances/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy("account_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy("account_list")

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = "finances/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy("account_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "finances/transaction_list.html"
    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get("category")
        account = self.request.GET.get("account")
        month = self.request.GET.get("month")
        year = self.request.GET.get("year")

        if category:
            queryset = queryset.filter(category=category)

        if account:
            queryset = queryset.filter(account=account)

        if month:
            queryset = queryset.filter(date__month=month, date__year=year)

        queryset = queryset.filter(user=self.request.user.id)
        return queryset

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.filter(user=self.request.user)
        categories = Category.objects.filter(user=self.request.user)
        accounts = Account.objects.filter(user=self.request.user)

        current_date = timezone.now()
        months = (
            transactions.values(
                "date__month",
            )
            .distinct()
            .order_by("-date__month")
        )
        years = (
            transactions.values(
                "date__year",
            )
            .distinct()
            .order_by("-date__year")
        )

        for month in months:
            month["month_name"] = calendar.month_name[month["date__month"]]

        context["current_date"] = current_date
        context["years"] = years
        context["months"] = months
        context["categories"] = categories
        context["accounts"] = accounts
        return context


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
            "type": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    }
                ),
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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields["account"].queryset = Account.objects.filter(user=user)
            self.fields["category"].queryset = Category.objects.filter(user=user)

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "finances/transaction_form.html"
    form_class = TransactionForm
    success_url = reverse_lazy("transaction_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = "finances/transaction_detail.html"


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    template_name = "finances/transaction_form.html"
    form_class = TransactionForm
    success_url = reverse_lazy("transaction_list")

    def form_valid(self, form):
        print('form valid')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(f'form invalid: {form.errors}, {form.non_field_errors()}')
        return response

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "finances/category_list.html"
    # paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "finances/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "finances/category_detail.html"


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "finances/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DashboardView(TemplateView):
    template_name = "finances/dashboard.html"

    def get_queryset(self):
        queryset = super(DashboardView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        accounts = Account.objects.filter(user=self.request.user)
        transactions = Transaction.objects.filter(user=self.request.user)
        categories = Category.objects.filter(user=self.request.user)

        recent_transactions = transactions.order_by("-created_at")[:5]

        category_spending = (
            categories.annotate(total=Sum("transactions__amount"))
            .filter(total__gt=0)
            .order_by("-total")[:5]
        )

        monthly_spending = transactions.filter(
            created_at__month=timezone.now().month
        ).aggregate(Sum("amount"))

        income = transactions.filter(
            type=Transaction.TransactionTypes.INCOME
        ).aggregate(income=Sum("amount"))["income"]

        expense = transactions.filter(
            type=Transaction.TransactionTypes.EXPENSE
        ).aggregate(expense=Sum("amount"))["expense"]

        net = income - expense
        total_balance = accounts.aggregate(Sum("balance"))

        context["recent_transactions"] = recent_transactions
        context["net"] = net
        context["category_spending"] = category_spending
        context["monthly_spending"] = monthly_spending
        context["categories"] = categories
        context["transactions"] = transactions
        context["accounts"] = accounts
        context["total_balance"] = total_balance
        return context
