import csv

from books.models import Book
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates sample test data."

    def handle(self, *args, **options):
        # Admin Login
        User.objects.create_superuser("admin", password="admin")

        path = settings.BASE_DIR / "data/books.csv"
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Book.objects.create(
                    title=row["title"],
                    libthing_id=row["libthing_id"],
                    last_name=row["last_name"],
                    first_name=row["first_name"],
                )
