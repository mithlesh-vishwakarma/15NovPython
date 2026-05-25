from django.urls import *
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("reg", reg, name="reg"),
    path("home", home, name="home"),
    path("logout", logout_user, name="logout"),
]
