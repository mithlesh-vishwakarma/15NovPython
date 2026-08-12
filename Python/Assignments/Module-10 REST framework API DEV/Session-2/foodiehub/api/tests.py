from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Restaurant


class RestaurantAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant = Restaurant.objects.create(
            name="Pizza Palace",
            cuisine="Italian",
            rating=4.5
        )
        self.list_url = '/api/restaurants/'
        self.detail_url = f'/api/restaurants/{self.restaurant.id}/'
        self.invalid_detail_url = '/api/restaurants/9999/'

    def test_list_restaurants_apiview(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Pizza Palace")

    def test_create_restaurant_apiview_success(self):
        data = {
            "name": "Burger Barn",
            "cuisine": "American",
            "rating": 4.2
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 2)

    def test_create_restaurant_apiview_failure(self):
        data = {
            "name": "",  # Invalid name
            "cuisine": "American"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_restaurant_detail_apiview_success(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Pizza Palace")

    def test_get_restaurant_detail_apiview_not_found(self):
        response = self.client.get(self.invalid_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_restaurant_apiview_success(self):
        data = {
            "name": "Pizza Palace Deluxe",
            "cuisine": "Italian-American",
            "rating": 4.8
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.name, "Pizza Palace Deluxe")

    def test_patch_restaurant_apiview_success(self):
        data = {"rating": 4.9}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.rating, 4.9)

    def test_delete_restaurant_apiview_success(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Restaurant.objects.filter(id=self.restaurant.id).exists())

    def test_delete_restaurant_apiview_not_found(self):
        response = self.client.delete(self.invalid_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RestaurantMixinViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant = Restaurant.objects.create(
            name="Sushi Spot",
            cuisine="Japanese",
            rating=4.7
        )
        self.mixin_list_url = '/api/restaurants/mixins/'
        self.mixin_detail_url = f'/api/restaurants/mixins/{self.restaurant.id}/'
        self.invalid_mixin_detail_url = '/api/restaurants/mixins/9999/'

    def test_list_restaurants_mixin(self):
        response = self.client.get(self.mixin_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_restaurant_mixin(self):
        data = {
            "name": "Taco Time",
            "cuisine": "Mexican",
            "rating": 4.3
        }
        response = self.client.post(self.mixin_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_restaurant_mixin(self):
        response = self.client.get(self.mixin_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Sushi Spot")

    def test_retrieve_restaurant_mixin_not_found(self):
        response = self.client.get(self.invalid_mixin_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_restaurant_mixin(self):
        data = {
            "name": "Super Sushi Spot",
            "cuisine": "Japanese Fusion",
            "rating": 4.9
        }
        response = self.client.put(self.mixin_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_restaurant_mixin(self):
        response = self.client.delete(self.mixin_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Restaurant.objects.filter(id=self.restaurant.id).exists())
