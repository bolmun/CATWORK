from django.db import models
from core import models as core_models


class Contract(core_models.TimeStampedModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "입양 계약서 내용 확인 중"),
        (STATUS_CONFIRMED, "입양 계약 확정"),
        (STATUS_CANCELED, "입양 계약 취소"),
    )

    status = models.CharField(
        max_length=30, choices=STATUS_CHOICE, blank=False, null=False
    )
    applicant = models.ForeignKey(
        "users.User", related_name="contracts", on_delete=models.CASCADE
    )
    care_taker = models.ForeignKey(
        "users.User", related_name="contracts_care", on_delete=models.CASCADE
    )

    cat = models.ForeignKey(
        "cats.Cat", related_name="contracts", on_delete=models.CASCADE
    )
    contents = models.TextField()
    agreed_applicant = models.BooleanField(default=False)
    agreed_care_taker = models.BooleanField(default=False)
