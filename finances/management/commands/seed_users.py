from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed Users"
    
    def handle(self, *args, **options):
        self.seed_users()

    def seed_users(self):
        user = User.objects.create_user(
            username = 'madayuki',
            email = "madayuki@mail.com",
            first_name = "madayuki",
            last_name = "hirata",
            password = "password"
        )
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {user.username} Users")
        )