from django.contrib import admin
from myapp.models import *
# Register your models here.

# class displayStudent():
#   list_display=("id","name","age","email")


admin.site.register(Student)