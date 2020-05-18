from django.core.management.base import BaseCommand
from cats.models import HealthCondition


class Command(BaseCommand):

    help = "This command helps to create health conditions"

    def handle(self, *args, **options):
        health_condition = [
            "눈곱이 자주껴요",
            "눈물을 흘려요",
            "귀지가 많은 편이에요",
            "콧물을 흘려요",
            "구토가 잦아요",
            "침을 흘려요",
            "잇몸 출혈이 있어요",
            "설사가 잦아요",
            "걸음이 불편해요",
            "장애가 있어요",
            "똥꼬발랄해요",
            "과체중이에요",
            "저체중이에요",
            "표준체중이에요",
            "전반적으로 양호해요",
        ]
        for h in health_condition:
            HealthCondition.objects.create(title=h)
        self.stdout.write(
            self.style.SUCCESS(f"{len(health_condition)} Health Conditions created!")
        )
