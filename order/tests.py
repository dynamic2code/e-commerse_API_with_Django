from django.test import TestCase, Client
from django.urls import reverse
from .models import Order
from customer.models import Customer
from .serializers import OrderSerializer
import json

class OrdersViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('orders')

    def test_get_orders(self):
        # Create some dummy orders
        customer = Customer.objects.create(username='test_user', phone_number='1234567890', email='testemail@gmail.com', password='sTrongP@ssword')
        Order.objects.create(item='Item 1', amount=10, customer_id = customer.customer_id)
        Order.objects.create(item='Item 2', amount=20, customer_id = customer.customer_id)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Assert that all orders are returned in response
        self.assertEqual(len(response.json()['data']), 2)

    def test_create_order_success(self):
        # Create a customer
        customer = Customer.objects.create(username='test_user', phone_number='1234567890', email='testemail@gmail.com', password='sTrongP@ssword')
        data = {'item': 'Test item', 'amount': 15, 'customer_id': customer.customer_id}
        response = self.client.post(self.url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        # Assert that the created order is returned in response
        self.assertEqual(response.json()['item'], 'Test item')
        self.assertEqual(response.json()['amount'], '15.00')

    def test_create_order_missing_customer_id(self):
        data = {'item': 'Test item', 'amount': 15}
        response = self.client.post(self.url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Missing customer ID')
