from django.contrib.auth.models import AbstractUser
from core import models as core_models
from django.db import models


class User(AbstractUser):

    """custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    is_personal_id = models.BooleanField(default=True)
    is_group_id = models.BooleanField(default=False)
