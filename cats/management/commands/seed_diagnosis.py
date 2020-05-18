from django.core.management.base import BaseCommand
from cats.models import Diagnosis


class Command(BaseCommand):

    help = "This command helps to create diagnosis"

    def handle(self, *args, **options):
        diagnosis = [
            "전염성 장염(범백혈구 감소증)",
            "전염성 복막염",
            "백혈병",
            "감기(허피스바이러스, 칼리시바이러스 등)",
            "독감",
            "심장사상충 감염",
            "톡소플라즈마 감염",
            "자궁축농증",
            "신부전증",
            "당뇨병",
            "갑상선기능항진증",
            "요로결석",
            "방광염",
            "췌장염",
            "비대성 심근증",
            "거대 결장증",
            "치주질환",
            "치아흡수성병변",
            "치아골절",
            "구내염",
            "여드름",
            "링웜",
            "외이염",
            "지방간증",
            "변비",
        ]
        for d in diagnosis:
            Diagnosis.objects.create(title=d)
        self.stdout.write(self.style.SUCCESS(f"{len(diagnosis)} Diagnosis created!"))
