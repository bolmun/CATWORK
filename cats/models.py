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

    name = models.CharField(max_length=30)
    city = models.CharField(max_length=80)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    is_neutered = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=10, default=0)
    skittishness = models.IntegerField()
    outgoingness = models.IntegerField()
    dominance = models.IntegerField()
    spontaneity = models.IntegerField()
    friendliness = models.IntegerField()
    mom_cat = models.ForeignKey(
        "self", blank=True, null=True, related_name="mom", on_delete=models.SET_NULL,
    )
    dad_cat = models.ForeignKey(
        "self", blank=True, null=True, related_name="dad", on_delete=models.SET_NULL,
    )
    bro_sis = models.ManyToManyField("self", related_name="bs_cat", blank=True)
    health_condition = models.ManyToManyField(HealthCondition, related_name="cats")
    diagnosis = models.ManyToManyField(Diagnosis, related_name="cats", blank=True)
    rescue_story = models.TextField()
    care_taker = models.ForeignKey(
        "users.User",
        blank=False,
        null=False,
        related_name="cats",
        on_delete=models.PROTECT,
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
