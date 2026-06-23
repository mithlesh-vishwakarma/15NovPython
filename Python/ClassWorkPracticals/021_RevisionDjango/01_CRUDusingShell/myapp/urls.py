from django.urls import path
from myapp.views import *
urlpatterns=[

  path("",index,name="index"),
  path("add_student",add_student,name="add_student"),
  path("display",display,name="display"),
  path("delete",delete,name="delete"),
  path("update",update,name="update")
]