from django.contrib import admin
from . import models


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = (
        "applicant",
        "care_taker",
        "cat",
        "status",
        "agreed_applicant",
        "agreed_care_taker",
    )

    list_filter = ("status",)
    search_fields = ("^applicant__username", "^care_taker__username", "cat")
    raw_id_fields = ("care_taker", "applicant", "cat")
    ordering = ("status", "cat")
