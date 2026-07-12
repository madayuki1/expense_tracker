from finances.models import Account
from django.contrib.auth.models import User
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

def SeedAccounts():
    created_count = 0
    users = User.objects.filter(is_superuser=False)
    for user in users:
        for account in ACCOUNTS:
            _, created = Account.objects.get_or_create(
                name = account['name'],
                balance = account['balance'],
                user = user,
            )
            if created :
                created_count += 1
    
    return created_count