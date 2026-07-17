from django.urls import path
from playlists.views import *

urlpatterns = [
    path("music/",home,name="index")
]
