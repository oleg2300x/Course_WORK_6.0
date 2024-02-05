from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin1',
            first_name='admin',
            last_name='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            email_verify=True,
        )

        user.set_password('admin')
        user.save()
