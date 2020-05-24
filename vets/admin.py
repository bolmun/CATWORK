from django.contrib import admin
from . import models


@admin.register(models.Vet)
class VetAdmin(admin.ModelAdmin):

    list_display = (
        "visit_date",
        "vet_title",
        "city",
        "cat",
        "is_vaccination",
        "visit_purpose",
    )

    raw_id_fields = ("cat",)

    list_filter = ("diagnosis",)

    ordering = (
        "cat",
        "vet_title",
        "city",
    )

    search_fields = ("=city", "=cat", "^vet_title")
