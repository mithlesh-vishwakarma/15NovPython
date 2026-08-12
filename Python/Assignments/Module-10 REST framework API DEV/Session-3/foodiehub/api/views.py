from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Restaurant
from api.serializers import RestaurantSerializer

class RestaurantPageNumberPagination(PageNumberPagination):
    page_size = 3

class RestaurantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer

    pagination_class = RestaurantLimitOffsetPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['cuisine']
    ordering_fields = ['name', 'cuisine']
    ordering = ['id']
