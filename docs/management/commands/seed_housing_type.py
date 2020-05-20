from django.core.management.base import BaseCommand
from docs.models import HousingType


class Command(BaseCommand):

    help = "This command helps to create housing types"

    def handle(self, *args, **options):
        housing_types = [
            "Flat",
            "Detached House",
            "Semi-detached House",
            "Terrace House",
        ]

        for h in housing_types:
            HousingType.objects.create(title=h)
        self.stdout.write(
            self.style.SUCCESS(f"{len(housing_types)} housing types created!")
        )
