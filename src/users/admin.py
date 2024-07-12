from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import User

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    list_display = ["email", "name", "is_admin", "is_active"]
    list_filter = ["is_admin", "is_active"]
    readonly_fields = ["created", "updated"]
    fieldsets = [
        (None, {"fields": ["email", "password", "created", "updated"]}),
        ("Personal info", {"fields": ["name"]}),
        ("Permissions", {"fields": ["is_admin", "is_active"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_admin",
                ],
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
