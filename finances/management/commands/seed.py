from django.core.management.base import BaseCommand
from finances.models import Category, Account, Transaction
from decimal import Decimal

CATEGORIES = [
    "Food",
    "Game",
    "School",
    "Work",
    "Shopping",
    "Movies",
    "Salary",
    "Invesment",
    "Other",
]
ACCOUNTS = [
    {
        "name": "BCA",
        "balance": 60000000
    },
    {
        "name": "Cash",
        "balance": 9000000
    },
    {
        "name": "Gopay",
        "balance": 100000
    },
    {
        "name": "Invesment",
        "balance": 5400000
    },
]

class Command(BaseCommand):
    help = "Seed default category"
    
    def handle(self, *args, **options):
        self.seed_categories()
        self.seed_account()

    def seed_categories(self):
        created_count = 0
        for category in CATEGORIES:
            _, created = Category.objects.get_or_create(
                name = category
            )
            if created :
                created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully Created {created_count} Categories")
        )

    def seed_account(self):
        created_count = 0
        for account in ACCOUNTS:
            _, created = Account.objects.get_or_create(
                name = account['name'],
                balance = account['balance']
            )
            if created :
                created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully Created {created_count} Accounts")
        )