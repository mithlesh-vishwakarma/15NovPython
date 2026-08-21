from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ExternalAPIEndpointsTestCase(APITestCase):

    def test_music_weather_endpoint(self):
        """Task 1 & Task 5: Test /api/music-weather/<city>/ returns temperature and description"""
        url = reverse('music-weather', kwargs={'city': 'London'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('temperature', response.data)
        self.assertIn('description', response.data)
        self.assertIn('city', response.data)
        self.assertIn('festival_tip', response.data)

    def test_food_location_success(self):
        """Task 2: Test /api/food-location/?name=Hard Rock Cafe returns coordinates"""
        url = reverse('food-location') + '?name=Hard Rock Cafe'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('latitude', response.data)
        self.assertIn('longitude', response.data)
        self.assertIn('restaurant', response.data)

    def test_food_location_missing_query_param(self):
        """Task 2: Test /api/food-location/ returns 400 when missing name parameter"""
        url = reverse('food-location')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_food_location_not_found(self):
        """Task 2: Test /api/food-location/ returns 404 when restaurant is not found"""
        url = reverse('food-location') + '?name=UnknownFakeRestaurant999'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_country_info_success(self):
        """Task 3: Test /api/country-info/<country_name>/ returns population and capital"""
        url = reverse('country-info', kwargs={'country_name': 'Japan'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('country', response.data)
        self.assertIn('capital', response.data)
        self.assertIn('population', response.data)

    def test_country_info_not_found(self):
        """Task 3: Test /api/country-info/<country_name>/ returns 404 for invalid country"""
        url = reverse('country-info', kwargs={'country_name': 'InvalidCountryXYZ99'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_github_repos_success(self):
        """Task 4: Test /api/github-repos/<username>/ returns list of repositories"""
        url = reverse('github-repos', kwargs={'username': 'torvalds'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)
        self.assertIn('repositories', response.data)
        self.assertIsInstance(response.data['repositories'], list)

    def test_github_repos_user_not_found(self):
        """Task 4: Test /api/github-repos/<username>/ returns 404 for invalid GitHub user"""
        url = reverse('github-repos', kwargs={'username': 'thisuserdefinitelydoesnotexist_99999'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)
