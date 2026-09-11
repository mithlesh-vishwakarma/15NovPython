from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',stundentData,name="stundentData"),
    path('delete',delete,name="delete"),
    path ('update',update,name="update"),
]