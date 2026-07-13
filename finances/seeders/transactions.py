
from django.contrib.auth.models import User
from finances.models import Category, Account, Transaction
from datetime import timedelta
from django.utils import timezone
from faker import Faker
import random

    
def SeedTransactions():
    created_count = 0 
    today = timezone.localdate()
    start_date = today - timedelta(days=60)
    types = Transaction.TransactionTypes.values
    users = list(User.objects.filter(is_superuser=False))
    fake = Faker()

    for user in users:
        accounts = list(Account.objects.filter(user=user))
        categories = list(Category.objects.filter(user=user))
        for _ in range(200):
            account = random.choice(accounts)
            category = random.choice(categories)
            type = random.choice(types)
            amount = random.randrange(10_000, 200_001, 10_000)
            date = start_date + timedelta(days=random.randint(0,60))
            description = fake.sentence(nb_words=10)
            name = fake.sentence(nb_words=3)

            Transaction.objects.create(
                account = account,
                category = category,
                type = type,
                user = user, 
                amount = amount,
                date = date,
                description = description,
                name = name
            )
            created_count += 1
    
    return created_count