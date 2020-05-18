from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    cats = models.ManyToManyField("cats.Cat", related_name="lists")

    def __str__(self):
        return self.title

    def count_cats(self):
        return self.cats.count()

    count_cats.short_description = "Number of Cats"
