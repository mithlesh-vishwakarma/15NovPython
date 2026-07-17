from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("search",search,name="search"),
    path("create",create,name="create"),
    path("destroy",destroy,name="destroy"),
    path("retrive",retrive,name="retrive"),
    path("update",update,name="update")
]
