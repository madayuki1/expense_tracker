from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed Users"
    
    def handle(self, *args, **options):
        self.seed_users()

    def seed_users(self):
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='admin'
        )
        user1 = User.objects.create_user(
            username = 'madayuki1',
            email = "madayuki@mail.com",
            first_name = "madayuki1",
            last_name = "hirata1",
            password = "password"
        )
        user2 = User.objects.create_user(
            username = 'madayuki2',
            email = "madayuki2@mail.com",
            first_name = "madayuki2",
            last_name = "hirata2",
            password = "password"
        )
        self.stdout.write(
            self.style.SUCCESS(f"Succesfully created {admin.username}, {user1.username} and {user2.username} Users")
        )