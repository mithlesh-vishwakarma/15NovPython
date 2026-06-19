from django.urls import path
from foodiespot.views import *

urlpatterns=[
  path("",index,name="index")
]