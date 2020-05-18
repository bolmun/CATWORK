from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "gender", "is_personal_id", "is_group_id",)},
        ),
    )

    list_filter = UserAdmin.list_filter + ("is_group_id",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_personal_id",
        "is_group_id",
    )
