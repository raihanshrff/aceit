from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "AceIT Information",
            {
                "fields": (
                    "full_name",
                    "role",
                    "experience_level",
                    "subscription_plan",
                    "created_at",
                )
            },
        ),
    )
    readonly_fields = ("created_at",)

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "AceIT Information",
            {
                "fields": (
                    "full_name",
                    "role",
                    "experience_level",
                    "subscription_plan",

                )
            },
        ),
    )