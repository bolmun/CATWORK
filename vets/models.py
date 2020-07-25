from django.db import models
from core import models as core_models


class Vet(core_models.TimeStampedModel):

    visit_date = models.DateField()
    vet_title = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    cat = models.ForeignKey("cats.Cat", related_name="vets", on_delete=models.CASCADE)
    is_vaccination = models.BooleanField()
    vaccination = models.CharField(max_length=100, blank=True, null=True)
    diagnosis = models.CharField(max_length=100, blank=True)
    prescription = models.TextField(blank=True)
    expense = models.IntegerField(blank=True, null=True)
    receipt = models.FileField(blank=True, null=True)

    def visit_purpose(self):
        vaccine = self.is_vaccination
        if vaccine == True:
            purpose = f"{self.vaccination}"
        else:
            purpose = f"{self.diagnosis}"
        return purpose

    def __str__(self):
        return f"{self.visit_date} | {self.vet_title} | {self.visit_purpose()}"
