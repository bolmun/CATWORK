from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "user",
        "count_cats",
    )

    search_fields = ("title",)

    filter_horizontal = ("cats",)
