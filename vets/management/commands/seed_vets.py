import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from vets import models as vet_models
from cats import models as cat_models


class Command(BaseCommand):

    help = "This command helps to create vet records"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many vet records you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_cats = cat_models.Cat.objects.all()
        seeder.add_entity(
            vet_models.Vet,
            number,
            {
                "cat": lambda x: random.choice(all_cats),
                "vet_title": lambda x: seeder.faker.company(),
                "visit_date": lambda x: datetime.now()
                - timedelta(days=random.randint(100, 1000)),
                "expense": lambda x: random.randint(5000, 3000000),
                "receipt": seeder.faker.file_name(),
                "diagnosis": lambda x: seeder.faker.word(),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} vet records created!"))
