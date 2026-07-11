from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from finances.models import Category, Account, Transaction
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed Transaction"
    accounts = list(Account.objects.all())
    categories = list(Category.objects.all())
    types = Transaction.TransactionTypes.values
    users = list(User.objects.filter(is_superuser=False))
    fake = Faker()
    
    def handle(self, *args, **options):
        self.seed_transactions()

    def seed_transactions(self):
        created_count = 0 
        for _ in range(200):
            account = random.choice(self.accounts)
            category = random.choice(self.categories)
            type = random.choice(self.types)
            amount = random.randrange(10_000, 200_001, 10_000)
            user = random.choice(self.users)
            description = self.fake.sentence(nb_words=10)
            name = self.fake.sentence(nb_words=3)

            Transaction.objects.create(
                account = account,
                category = category,
                type = type,
                user = user, 
                amount = amount,
                description = description,
                name = name
            )
            created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {created_count} Transaction")
        )