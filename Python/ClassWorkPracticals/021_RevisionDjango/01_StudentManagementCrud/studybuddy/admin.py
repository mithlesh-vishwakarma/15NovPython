from django.contrib import admin
from studybuddy.models import *

class Display_student(admin.ModelAdmin):
  list_display=["student_id","first_name","last_name","date_of_birth","email","phone","course","admission_date"]

admin.site.register(Student,Display_student)
admin.site.register(Course)
admin.site.register(Subject)


