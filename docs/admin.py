from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.HousingType)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.docs.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Doc)
class DocAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "cat",
                    "applicant",
                    "phone",
                    "birthdate",
                    "address",
                    "id_card",
                    "instagram_id",
                )
            },
        ),
        (
            "Cirumstance",
            {
                "fields": (
                    "housing_type",
                    "is_rented",
                    "landlord_agree",
                    "protect_window",
                    "protect_door",
                )
            },
        ),
        (
            "Finance Info",
            {
                "fields": (
                    "job",
                    "company_title",
                    "job_certification",
                    "budget_plan",
                    "insurance_plan",
                )
            },
        ),
        (
            "Family Info",
            {
                "fields": (
                    "married",
                    "family_num",
                    "children_num",
                    "current_cat",
                    "other_companion_animals",
                )
            },
        ),
        ("Experience", {"fields": ("first_ever_cat", "reason_adopt")},),
    )

    list_display = (
        "applicant",
        "cat",
        "address",
        "birthdate",
        "housing_type",
        "is_rented",
        "job",
    )

    raw_id_fields = ("cat", "applicant")
    inlines = (PhotoInline,)
    ordering = (
        "cat",
        "applicant",
        "address",
        "birthdate",
        "housing_type",
        "is_rented",
        "job",
    )

    search_fields = ("=cat", "^applicant__username")

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
