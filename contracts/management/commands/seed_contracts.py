import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from cats import models as cat_models
from contracts import models as contract_models


class Command(BaseCommand):

    help = "This command helps to create contracts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many contracts you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_cats = cat_models.Cat.objects.all()
        seeder.add_entity(
            contract_models.Contract,
            number,
            {
                "applicant": lambda x: random.choice(all_users),
                "care_taker": lambda x: random.choice(all_users),
                "cat": lambda x: random.choice(all_cats),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} contracts created!"))
