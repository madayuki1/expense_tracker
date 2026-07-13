from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Account(models.Model):
    """Model definition for Account."""

    # TODO: Define fields here
    name = models.CharField("Account Name", max_length=50)
    balance = models.DecimalField("Account Balance", max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Account."""

        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        """Unicode representation of Account."""
        return self.name

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField("Category Name", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Transaction(models.Model):
    class Meta:
        """Meta definition for Transaction."""

        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    class TransactionTypes(models.TextChoices):
        EXPENSE = "expense", "Expense"
        INCOME = "income", "Income"
        TRANSFER = "transfer", "Transfer"

    # TODO: Define fields here
    name = models.CharField("name", max_length=50, null=True, blank=True)
    account = models.ForeignKey(
        "finances.Account",
        verbose_name="Account ID",
        on_delete=models.CASCADE,
        default=1,
        related_name="transactions",
    )
    category = models.ForeignKey(
        "finances.Category",
        verbose_name="Category ID",
        on_delete=models.CASCADE,
        default=1,
        related_name="transactions",
    )
    type = models.CharField(
        max_length=10,
        choices=TransactionTypes.choices,
        default=TransactionTypes.EXPENSE,
    )
    amount = models.DecimalField("Transaction Amount", max_digits=9, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField("Transaction Description", max_length=100)
    date = models.DateField("Transaction Date", default=timezone.localdate())
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    def __str__(self):
        """Unicode representation of Transaction."""
        return self.name

class Budget(models.Model):
    """Model definition for Budget."""
    class BudgetTypes(models.TextChoices):
        WEEKLY = "weekly", "Weekly"
        MONTHLY = "monthly", "Monthly"
        YEARLY = "yearly", "Monthly"

    # TODO: Define fields here
    name = models.CharField("Budget Name", max_length=50)
    limit = models.DecimalField("Budget Limit", max_digits=9, decimal_places=2)
    category = models.ForeignKey(
        "finances.Category", 
        verbose_name='Category ID', 
        on_delete=models.CASCADE, 
        default=1,
        related_name="transactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(
        max_length=10,
        choice=BudgetTypes.choices,
        default=BudgetTypes.MONTHLY
        )

    class Meta:
        """Meta definition for Budget."""

        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'

    def __str__(self):
        """Unicode representation of Budget."""
        pass
