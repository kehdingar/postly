from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.core import mail


User = get_user_model()

class UserTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='kehdinga',
            email='kehdingar@gmail.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )    

    def test_create_user(self):
        url = reverse('register')
        data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password': 'test2pass123',
            'first_name': 'Test2',
            'last_name': 'User2'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='testuser2').username, 'testuser2')

    def test_obtain_token(self):
        url = reverse('api_token_auth')
        data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_password_reset(self):
        # Request a password reset token for the test user
        url = reverse('password_reset:reset-password-request')
        data = {'email': self.user.email}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the password reset email was sent to the test user's email address
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertIn(self.user.email, message.to)        