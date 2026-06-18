from django.urls import path
from myapp.views import *
urlpatterns=[

  path("",index,name="index"),
  path("add_student",add_student,name="add_student")
]