from django.urls import path
from student_management_system.views import *

urlpatterns = [
  path("",index,name="index"),
  path("add_student/",add_student, name="add_student"),
  path("display_data/",display_data,name="display_data"),
  path("update_data/<int:id>/",update_data,name="update_data"),
  path("delete_data/<int:id>/",delete_data,name="delete_data"),
]
