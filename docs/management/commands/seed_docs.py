import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from cats import models as cat_models
from users import models as user_models
from docs import models as doc_models


class Command(BaseCommand):

    help = "This command helps to create docs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many docs you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_cats = cat_models.Cat.objects.all()
        housing_types = doc_models.HousingType.objects.all()
        seeder.add_entity(
            doc_models.Doc,
            number,
            {
                "applicant": lambda x: random.choice(all_users),
                "housing_type": lambda x: random.choice(housing_types),
                "phone": lambda x: seeder.faker.phone_number(),
                "id_card": lambda x: seeder.faker.file_name(),
                "job_certification": lambda x: seeder.faker.file_name(),
                "company_title": lambda x: seeder.faker.company(),
                "instagram_id": lambda x: seeder.faker.word(),
                "job": lambda x: seeder.faker.job(),
                "address": lambda x: seeder.faker.address(),
                "cat": lambda x: random.choice(all_cats),
                "family_num": lambda x: random.randint(1, 10),
                "children_num": lambda x: random.randint(0, 10),
                "current_cat": lambda x: random.randint(0, 10),
                "other_companion_animals": lambda x: random.randint(0, 10),
                "budget_plan": lambda x: random.randint(100000, 10000000),
            },
        )

        created_docs = seeder.execute()
        created_clean = flatten(list(created_docs.values()))
        for pk in created_clean:
            home = doc_models.Doc.objects.get(pk=pk)
            for i in range(2, random.randint(4, 6)):
                doc_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"home_photos/{random.randint(1,15)}.jpg",
                    home=home,
                )

        self.stdout.write(self.style.SUCCESS(f"{number} docs created!"))
