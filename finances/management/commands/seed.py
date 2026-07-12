from django.core.management.base import BaseCommand
from finances.seeders.accounts import SeedAccounts
from finances.seeders.categories import SeedCategories
from finances.seeders.users import SeedUsers
from finances.seeders.transactions import SeedTransactions

class Command(BaseCommand):
    help = "Seed default category, account"
    
    def handle(self, *args, **options):
        users_created = SeedUsers()
        accounts_created = SeedAccounts()
        categories_created = SeedCategories()
        transactions_created = SeedTransactions()

        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {users_created} Users")
        )
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {accounts_created} Accounts")
        )
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {categories_created} Categories")
        )
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {transactions_created} Transactions")
        )
