from django.urls import path
from myapp.views import index, get_students, add_student, update_student, delete_student

urlpatterns = [
    path("", index, name="index"),
    path("get-students/", get_students, name="get_students"),
    path("add-student/", add_student, name="add_student"),
    path("update-student/", update_student, name="update_student"),
    path("delete-student/", delete_student, name="delete_student"),
]