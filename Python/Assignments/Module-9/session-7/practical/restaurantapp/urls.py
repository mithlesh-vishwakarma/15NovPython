from django.urls import path
from restaurantapp.views import *

urlpatterns = [
    path("",index,name="index")
]
