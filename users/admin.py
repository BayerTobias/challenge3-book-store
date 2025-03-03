from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUser_Admin(UserAdmin):
    list_display = ("id", "username", "author_pseudonym")
    list_display_links = ("id", "username", "author_pseudonym")
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("author_pseudonym",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("author_pseudonym",)}),
    )


admin.site.register(CustomUser, CustomUser_Admin)
