from django.urls import path
from . import views

urlpatterns = [
    # Task 1: Music weather for a city
    path('music-weather/<str:city>/', views.music_weather, name='music-weather'),
    
    # Task 2: Food location geocoding
    path('food-location/', views.food_location, name='food-location'),
    
    # Task 3: Country quick facts info
    path('country-info/<str:country_name>/', views.country_info, name='country-info'),
    
    # Task 4: GitHub repositories lookup
    path('github-repos/<str:username>/', views.github_repos, name='github-repos'),
]




# urlsAPi
# -------------------

# http://127.0.0.1:8000/api/music-weather/London/
# http://127.0.0.1:8000/api/food-location/?name=Hard%20Rock%20Cafe
# http://127.0.0.1:8000/api/country-info/Japan/
# http://127.0.0.1:8000/api/github-repos/torvalds/