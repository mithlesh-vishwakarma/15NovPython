from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Playlist, Order, CartItem, Ticket

User = get_user_model()


class AuthenticationAndPermissionTests(TestCase):

    def setUp(self):
        # Create standard user
        self.user = User.objects.create_user(
            username='regularuser',
            password='password123',
            is_premium=False
        )

        # Create premium user
        self.premium_user = User.objects.create_user(
            username='premiumuser',
            password='password123',
            is_premium=True
        )

        # Generate auth token for regular user (Task 2)
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()

    # --- Task 1: BasicAuthentication for /api/playlists/ ---
    def test_playlists_without_authentication(self):
        response = self.client.get('/api/playlists/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_playlists_with_basic_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + 'cmVndWxhcnVzZXI6cGFzc3dvcmQxMjM=') # base64 for regularuser:password123
        response = self.client.get('/api/playlists/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- Task 2: TokenAuthentication for /api/orders/ ---
    def test_orders_without_token(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_orders_with_valid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- Task 3: SessionAuthentication for /api/cart/ ---
    def test_cart_unauthenticated_returns_forbidden_or_unauthorized(self):
        response = self.client.get('/api/cart/')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_cart_authenticated_user_can_access(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- Task 4: Custom IsPremiumUser permission for /api/tickets/ ---
    def test_tickets_non_premium_user_access(self):
        self.client.force_login(self.user) # is_premium=False
        response = self.client.get('/api/tickets/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_tickets_premium_user_access(self):
        self.client.force_login(self.premium_user) # is_premium=True
        response = self.client.get('/api/tickets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
