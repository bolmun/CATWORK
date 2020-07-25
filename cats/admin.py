from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.HealthCondition, models.Diagnosis, models.Appearance)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.cats.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "city",
                    "birthdate",
                    "estimated_age",
                    "gender",
                    "is_neutered",
                    "barcode",
                    "appearance",
                    "foster_needed",
                )
            },
        ),
        ("Health", {"fields": ("health_condition", "diagnosis")},),
        (
            "Characteristic",
            {
                "fields": (
                    "skittishness",
                    "outgoingness",
                    "dominance",
                    "spontaneity",
                    "friendliness",
                    "care_category",
                )
            },
        ),
        ("Family Info", {"fields": ("mom_cat", "dad_cat", "bro_sis")},),
        ("More Detail", {"fields": ("rescue_story", "care_taker")},),
        ("Latest Status", {"fields": ("adopted",)}),
    )

    list_display = (
        "name",
        "city",
        "gender",
        "is_neutered",
        "birthdate",
        "count_age",
        "estimated_age",
        "care_taker",
        "care_category",
        "foster_needed",
    )

    raw_id_fields = ("care_taker",)

    list_filter = ("health_condition", "diagnosis", "appearance", "foster_needed")

    filter_horizontal = ("health_condition", "diagnosis", "bro_sis")

    inlines = (PhotoInline,)

    ordering = (
        "city",
        "gender",
        "is_neutered",
        "skittishness",
        "outgoingness",
        "dominance",
        "spontaneity",
        "friendliness",
    )

    search_fields = ("=city", "^care_taker__username", "=name")

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
