from django.core.management.base import BaseCommand
from finances.models import Category, Account, Transaction
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed Transaction"
    accounts = list(Account.objects.all())
    categories = list(Category.objects.all())
    fake = Faker()
    
    def handle(self, *args, **options):
        self.seed_transactions()

    def seed_transactions(self):
        created_count = 0 
        for _ in range(20):
            account = random.choice(self.accounts)
            category = random.choice(self.categories)
            amount = random.randint(10000, 200000)
            description = self.fake.sentence(nb_words=10)
            name = self.fake.sentence(nb_words=3)

            Transaction.objects.create(
                account = account,
                category = category,
                amount = amount,
                description = description,
                name = name
            )
            created_count += 1
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {created_count} Transaction")
        )