from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer
from .serializer import SignUpSerializer, LoginSerializer, CustomerSerializer
from django.contrib.auth.hashers import make_password

class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('sign_up')

    def test_sign_up_success(self):
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'TestPassword123',
            'phone_number': '1234567890'
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_sign_up_invalid_data(self):
        # Test with invalid data
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'short',  # Password too short
            'phone_number': '1234567890'
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user = Customer.objects.create(
            username='test_user',
            email='test@example.com',
            password=make_password('TestPassword123'),
            phone_number='1234567890'
        )
        self.url = reverse('log_in')

    def test_login_success(self):
        data = {
            'email': 'test@example.com',
            'password': 'TestPassword123',
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Assert that token and user data are returned in response
        self.assertIn('token', response.json())
        self.assertIn('user', response.json())

    def test_login_invalid_credentials(self):
        # Test with invalid credentials
        data = {
            'email': 'test@example.com',
            'password': 'WrongPassword',
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Add more test cases as needed...

class CustomerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('customer')

    def test_customer_get(self):
        # Create some dummy customers
        Customer.objects.create(
            username='customer1',
            email='customer1@example.com',
            password=make_password('CustomerPassword123'),
            phone_number='1234567890'
        )
        Customer.objects.create(
            username='customer2',
            email='customer2@example.com',
            password=make_password('CustomerPassword123'),
            phone_number='1234567890'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Assert that all customers are returned in response
        self.assertEqual(len(response.json()), 2)
