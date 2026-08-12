from django.urls import path

from api.views import (
    RestaurantListCreateAPIView,
    RestaurantDetailAPIView,
    RestaurantListCreateMixinView,
    RestaurantDetailMixinView,
)

urlpatterns = [
    # Task 3 & 4: APIView Endpoints
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
    path('restaurants/apiview/', RestaurantListCreateAPIView.as_view(), name='restaurant-apiview-list-create'),
    path('restaurants/apiview/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-apiview-detail'),

    # Task 5: GenericAPIView + Mixins Refactored Endpoints
    path('restaurants/mixins/', RestaurantListCreateMixinView.as_view(), name='restaurant-mixin-list-create'),
    path('restaurants/mixins/<int:pk>/', RestaurantDetailMixinView.as_view(), name='restaurant-mixin-detail'),
]
