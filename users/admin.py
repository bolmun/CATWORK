from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("avatar", "gender", "login_method",)},),
        (
            "Status",
            {"fields": ("is_group_id", "foster_available", "adoption_available",)},
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "is_group_id",
        "foster_available",
        "adoption_available",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_group_id",
        "foster_available",
        "adoption_available",
        "email_verified",
        "email_secret",
        "login_method",
    )
