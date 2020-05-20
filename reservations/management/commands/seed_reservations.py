import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from docs import models as doc_models
from reservations import models as reservation_models


class Command(BaseCommand):

    help = "This command helps to create reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many resevations you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_docs = doc_models.Doc.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "doc": lambda x: random.choice(all_docs),
                "meeting_address": lambda x: seeder.faker.address(),
                "meeting_time": lambda x: datetime.now()
                - timedelta(hours=random.randint(0, 24)),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
