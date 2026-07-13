from finances.models import Budget, Account, Category
from django.contrib.auth.models import User
from faker import Faker
import random

def SeedBudgets():
    created_count = 0
    fake = Faker()
    users = User.objects.filter(is_superuser=False)
    types = Budget.BudgetTypes.values

    for user in users:
        categories = Category.objects.filter(user=user)
        for _ in range(4):
            name = fake.word()
            limit = random.randrange(500_000, 3_000_000, 500_000)
            category = random.choice(categories)
            type = random.choice(types)

            Budget.objects.create(
                name = name,
                limit = limit,
                category = category,
                user = user,
                type = type
            )
            created_count += 1

    return created_count