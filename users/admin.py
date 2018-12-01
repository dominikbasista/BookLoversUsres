from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "place_of_live", "education", "gender","about_be",
                    "age", "favorite_categories", "favorite_writers"]


admin.site.register(UserProfile, UserAdmin)

