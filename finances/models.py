from django.db import models

# Create your models here.
class Account(models.Model):
    """Model definition for Account."""

    # TODO: Define fields here
    name = models.CharField("Account Name", max_length=50)
    balance = models.DecimalField("Account Balance", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Account."""

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        """Unicode representation of Account."""
        return self.name

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField("Category Name", max_length=50)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Transaction(models.Model):
    """Model definition for Transaction."""

    # TODO: Define fields here
    name = models.CharField("name", max_length=50, null=True, blank=True)
    account = models.ForeignKey("finances.Account", verbose_name="Account ID", on_delete=models.CASCADE)
    category = models.ForeignKey("finances.Category", verbose_name="Category ID", on_delete=models.CASCADE)
    amount = models.DecimalField("Transaction Amount", max_digits=9, decimal_places=2)
    description = models.CharField("Transaction Description", max_length=100)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transaction."""
        return self.name