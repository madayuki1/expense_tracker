from finances.models import Category
from django.contrib.auth.models import User

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

def SeedCategories():
    created_count = 0
    users = User.objects.filter(is_superuser=False)
    for user in users: 
        for category in CATEGORIES:
            _, created = Category.objects.get_or_create(
                name = category,
                user = user
            )
            if created :
                created_count += 1
    
    return created_count