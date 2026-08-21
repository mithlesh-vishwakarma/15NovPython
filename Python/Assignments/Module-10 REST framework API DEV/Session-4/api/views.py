from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Playlist, Order, CartItem, Ticket
from .serializers import PlaylistSerializer, OrderSerializer, CartItemSerializer, TicketSerializer
from .permissions import IsPremiumUser

# Task 1: Music App Playlists Endpoint (BasicAuthentication)
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Task 2: Zomato-style Food Ordering Endpoint (TokenAuthentication)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Task 3: Flipkart-style Shopping Cart Endpoint (SessionAuthentication)
class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Task 4: BookMyShow-style Ticket Booking Endpoint (Custom IsPremiumUser Permission)
class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # Allow Token, Session, or Basic auth to identify the user
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsPremiumUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
