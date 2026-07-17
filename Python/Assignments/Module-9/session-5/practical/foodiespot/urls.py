from django.urls import path
from foodiespot.views import index
urlpatterns=[
  path("",index,name="index")
]