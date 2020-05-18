from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HealthCondition(AbstractItem):
    class Meta:
        verbose_name_plural = "Health Condition"


class Diagnosis(AbstractItem):
    class Meta:
        verbose_name_plural = "Diagnosis"


class Cat(core_models.TimeStampedModel):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=80)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    is_neutered = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    skittishness = models.IntegerField()
    outgoingness = models.IntegerField()
    dominance = models.IntegerField()
    spontaneity = models.IntegerField()
    friendliness = models.IntegerField()
    health_condition = models.ManyToManyField(HealthCondition, related_name="cats")
    diagnosis = models.ManyToManyField(
        Diagnosis, related_name="cats", blank=True, null=True
    )
    rescue_story = models.TextField()
    care_taker = models.ForeignKey(
        "users.User",
        blank=False,
        null=False,
        related_name="cats",
        on_delete=models.PROTECT,
    )
    mom = models.ForeignKey(
        "Cat", null=True, related_name="cats_mom", blank=True, on_delete=models.PROTECT
    )
    dad = models.ForeignKey(
        "Cat", null=True, related_name="cats_dad", blank=True, on_delete=models.PROTECT
    )
    bro_sis = models.ManyToManyField(
        "Cat", related_name="cats_bs", blank=True, null=True
    )

    children = models.ManyToManyField(
        "Cat", related_name="cats_child", blank=True, null=True
    )
    barcode = models.IntegerField(blank=True, null=True)
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cat_photos")
    cat = models.ForeignKey("Cat", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
