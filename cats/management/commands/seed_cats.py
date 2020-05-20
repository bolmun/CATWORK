import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from cats import models as cat_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command helps to create cats"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many cats you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_cats = cat_models.Cat.objects.all()
        seeder.add_entity(
            cat_models.Cat,
            number,
            {
                "name": lambda x: seeder.faker.name(),
                "birthdate": lambda x: datetime.now()
                - timedelta(days=random.randint(100, 1000)),
                "care_taker": lambda x: random.choice(all_users),
                "skittishness": lambda x: random.randint(1, 5),
                "outgoingness": lambda x: random.randint(1, 5),
                "dominance": lambda x: random.randint(1, 5),
                "spontaneity": lambda x: random.randint(1, 5),
                "friendliness": lambda x: random.randint(1, 5),
                "barcode": lambda x: random.randint(100000, 999999),
                "adopted": False,
                "mom_cat": lambda x: random.choice(all_cats),
                "dad_cat": lambda x: random.choice(all_cats),
            },
        )

        created_cats = seeder.execute()
        created_clean = flatten(list(created_cats.values()))
        health_condition = cat_models.HealthCondition.objects.all()
        diagnosis = cat_models.Diagnosis.objects.all()
        for pk in created_clean:
            cat = cat_models.Cat.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                cat_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"cat_photos/{random.randint(1,13)}.webp",
                    cat=cat,
                )
            for h in health_condition:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    cat.health_condition.add(h)

            for d in diagnosis:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    cat.diagnosis.add(d)

        self.stdout.write(self.style.SUCCESS(f"{number} cats created!"))
