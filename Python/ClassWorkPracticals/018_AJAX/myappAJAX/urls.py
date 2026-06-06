from django.urls import path
from myappAJAX.views import *

urlpatterns = [
    path("", index, name="index"),
    path("test", test, name="test"),
    path("search", search, name="search"),
    path("countries", get_countries, name="countries"),
    path("states", get_states, name="states"),
    path("cities", get_cities, name="cities"),
]
