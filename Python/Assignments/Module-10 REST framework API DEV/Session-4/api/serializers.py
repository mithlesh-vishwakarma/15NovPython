from rest_framework import serializers
from .models import Playlist, Order, CartItem, Ticket

# Serializer for Playlist (Task 1)
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'user']
        read_only_fields = ['user']

# Serializer for Order (Task 2)
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'restaurant_name', 'item_name', 'amount', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

# Serializer for CartItem (Task 3)
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'quantity', 'price', 'user']
        read_only_fields = ['user']

# Serializer for Ticket (Task 4)
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'movie_title', 'seat_number', 'price', 'user']
        read_only_fields = ['user']
