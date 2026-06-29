from django.core.management.base import BaseCommand
from finances.models import Category, Account, Transaction
from django.contrib.auth.models import User
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
        "balance": 60000000,
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

USERS = [
    {
        "username": "madayuki",
        "email" : "madayuki@email.com",
        "first_name" : "madayuki",
        "last_name" : "hirata",
        "password" : "password",
    }
]
class Command(BaseCommand):
    help = "Seed default category, account, user"
    
    def handle(self, *args, **options):
        self.user = User.objects.create_user(
            username = 'madayuki',
            email = "madayuki@mail.com",
            first_name = "madayuki",
            last_name = "hirata",
            password = "password"
        )
        self.seed_categories()
        self.seed_account()

    def seed_categories(self):
        created_count = 0
        for category in CATEGORIES:
            _, created = Category.objects.get_or_create(
                name = category,
                user = self.user
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
                balance = account['balance'],
                user = self.user,
            )
            if created :
                created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully Created {created_count} Accounts")
        )

    def seed_user(self):
        created_count = 0
        for user in USERS:
            _, created = User.objects.create_user(
                username = user['username'],
                email = user['email'],
                first_name = user['first_name'],
                last_name = user['last_name'],
                password = user['password']
            )
            if created :
                created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully Created {created_count} Users")
        )