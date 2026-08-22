from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)

# @admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "specialization",
        "email",
        "city",
        "experience",
        "available",
    )

    search_fields = (
        "name",
        "specialization",
        "city",
    )

    list_filter = (
        "specialization",
        "city",
        "available",
    )