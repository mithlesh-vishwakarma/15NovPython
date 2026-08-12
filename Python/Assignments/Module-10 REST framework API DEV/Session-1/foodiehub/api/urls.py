from django.urls import path
from api.views import hello_spotify

urlpatterns = [
    path('hello_spotify/', hello_spotify, name='hello_spotify'),
]
