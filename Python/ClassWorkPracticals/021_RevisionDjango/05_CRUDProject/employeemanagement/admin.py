from django.contrib import admin
from employeemanagement.models import *

# Register your models here.

class displayHeader(admin.ModelAdmin):
    list_display=["name","email","designation"]

admin.site.register(Employee,displayHeader)