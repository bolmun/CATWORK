import math
from datetime import date
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


class Appearance(AbstractItem):
    class Meta:
        verbose_name_plural = "Appearance"


class Cat(core_models.TimeStampedModel):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    BLUE_CARE = "blue care"
    GREEN_CARE = "green care"
    ORANGE_CARE = "orange care"
    PINK_CARE = "pink care"

    CARE_CHOICES = (
        (BLUE_CARE, "Blue Care"),
        (GREEN_CARE, "Green Care"),
        (ORANGE_CARE, "Orange Care"),
        (PINK_CARE, "Pink Care"),
    )

    name = models.CharField(max_length=30)
    city = models.CharField(max_length=80)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    is_neutered = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    estimated_age = models.CharField(max_length=10, default=0)
    appearance = models.ForeignKey(
        Appearance, related_name="cats", null=True, on_delete=models.SET_NULL
    )
    skittishness = models.IntegerField()
    outgoingness = models.IntegerField()
    dominance = models.IntegerField()
    spontaneity = models.IntegerField()
    friendliness = models.IntegerField()
    care_category = models.CharField(
        choices=CARE_CHOICES, default=GREEN_CARE, max_length=12
    )
    foster_needed = models.BooleanField(default=False)
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
        default="admin",
        on_delete=models.SET_DEFAULT,
    )

    barcode = models.IntegerField(blank=True, null=True)
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cats:detail", kwargs={"pk": self.pk})

    def count_age(self):
        now = date.today()
        birth = self.birthdate
        if birth != None:
            difference = now - birth
            if difference.days > 365:
                year_age = math.floor((difference.days) / 365)
                age = f"{year_age} year(s) old"
            else:
                month_age = math.floor((difference.days) / 30)
                age = f"{month_age} months"
        else:
            age = self.estimated_age
        return age

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cat_photos")
    cat = models.ForeignKey("Cat", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
