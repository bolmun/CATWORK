from django.db import models
from core import models as core_models
from phonenumber_field.modelfields import PhoneNumberField


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HousingType(AbstractItem):
    class Meta:
        verbose_name_plural = "House Types"


class Doc(core_models.TimeStampedModel):

    applicant = models.ForeignKey(
        "users.User", related_name="docs", on_delete=models.CASCADE
    )
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    cat = models.ForeignKey("cats.Cat", related_name="docs", on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    housing_type = models.ForeignKey(
        HousingType, related_name="docs", on_delete=models.CASCADE
    )
    is_rented = models.BooleanField(default=False)
    landlord_agree = models.BooleanField(default=True)
    job = models.CharField(max_length=100)
    company_title = models.CharField(max_length=100, blank=True, null=True)
    id_card = models.ImageField()
    job_certification = models.ImageField(blank=True, null=True)
    instagram_id = models.CharField(max_length=15, blank=True, null=True)
    married = models.BooleanField(default=False)
    family_num = models.IntegerField()
    children_num = models.IntegerField()
    current_cat = models.IntegerField()
    first_ever_cat = models.BooleanField(default=False)
    other_companion_animals = models.IntegerField()
    budget_plan = models.IntegerField()
    insurance_plan = models.BooleanField(default=True)
    protect_window = models.BooleanField(default=True)
    protect_door = models.BooleanField(default=True)
    reason_adopt = models.TextField()

    def __str__(self):
        return f"{self.applicant}님 | {self.cat} Foster application"


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="home_photos")
    home = models.ForeignKey("Doc", related_name="photos_doc", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
