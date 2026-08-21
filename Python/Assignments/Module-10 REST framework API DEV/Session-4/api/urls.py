from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    PlaylistListCreateView,
    OrderListCreateView,
    CartItemListCreateView,
    TicketListCreateView,
)

urlpatterns = [
    # Task 1: Music App Playlists (BasicAuthentication)
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    
    # Task 2: Zomato-style Food Ordering (TokenAuthentication)
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # Task 3: Flipkart-style Shopping Cart (SessionAuthentication)
    path('cart/', CartItemListCreateView.as_view(), name='cart-list'),
    
    # Task 4: BookMyShow-style Ticket Booking (IsPremiumUser Custom Permission)
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list'),
]


# Task 1 (BasicAuth Playlists): http://127.0.0.1:8000/api/playlists/
# Task 2 (TokenAuth Orders): http://127.0.0.1:8000/api/orders/
# Task 2 (Obtain Token): http://127.0.0.1:8000/api/api-token-auth/
# Task 3 (SessionAuth Cart): http://127.0.0.1:8000/api/cart/
# Task 4 (IsPremiumUser Tickets): http://127.0.0.1:8000/api/tickets/