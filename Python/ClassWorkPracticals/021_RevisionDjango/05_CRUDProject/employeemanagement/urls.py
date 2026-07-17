from django.urls import path
from employeemanagement.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",create,name="create"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("update",update,name="update")
]
