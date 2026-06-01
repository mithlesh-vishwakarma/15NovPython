from django.urls import path
from myappAJAX.views import *

urlpatterns = [
    path('',index,name="index"),
    path("test",test,name="test")
]
