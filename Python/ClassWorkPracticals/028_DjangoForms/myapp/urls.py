from django.urls import path
from myapp.views import stundentData

urlpatterns = [
    path('',stundentData,name="stundentData")
]