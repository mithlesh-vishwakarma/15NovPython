from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class APIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_send_email_success(self):
        url = '/api/send-email/'
        data = {'email': 'testuser@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('status', response.data)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('mailgun_id', response.data)

    def test_send_email_invalid(self):
        url = '/api/send-email/'
        data = {'email': 'invalid-email-string'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_send_sms_success(self):
        url = '/api/send-sms/'
        data = {
            'phone_number': '+15551234567',
            'message': 'Welcome! Your verification code is 123456.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('sid', response.data)

    def test_send_sms_missing_field(self):
        url = '/api/send-sms/'
        data = {'phone_number': '+15551234567'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pay_success(self):
        url = '/api/pay/'
        data = {
            'amount': 49.99,
            'currency': 'usd'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'succeeded')
        self.assertIn('transaction_id', response.data)
        self.assertEqual(response.data['amount'], 49.99)

    def test_pay_invalid_amount(self):
        url = '/api/pay/'
        data = {
            'amount': 'not-a-number',
            'currency': 'usd'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_google_login_success(self):
        url = '/api/google-login/'
        data = {
            'email': 'google_test_user@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])
        self.assertIn('refresh', response.data['tokens'])
        
        # Verify user created in DB
        self.assertTrue(User.objects.filter(email='google_test_user@example.com').exists())
