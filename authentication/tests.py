from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.


User = get_user_model()

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_user_registration(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword123',
            'password_confirm': 'testpassword123'
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_user_login(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        data = {
            'email': 'test@example.com',
            'password': 'testpassword123'
        }
        response = self.client.post('/api/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)