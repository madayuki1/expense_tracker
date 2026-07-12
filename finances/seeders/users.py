from django.contrib.auth.models import User

def SeedUsers():
    created = []
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
    created.append(admin.username)
    created.append(user1.username)
    created.append(user2.username)
    return created