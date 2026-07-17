from django.urls import path
from AjaxApp.views import *

urlpatterns=[
    path("",index,name="index")

]