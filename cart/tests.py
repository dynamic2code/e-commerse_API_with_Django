from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Cart, CartItem, Product
from .views import CartView, CartItemView
from customer.models import Customer

class CartViewTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(username='test_user', password='test_password')

    def test_get_cart_success(self):
        cart = Cart.objects.create(customer=self.customer)
        url = reverse('cart', kwargs={'user_id': self.customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer'], self.customer.id)

    def test_get_cart_not_found(self):
        url = reverse('cart', kwargs={'user_id': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Cart does not exist')

class CartItemViewTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(username='test_user', password='test_password')
        self.cart = Cart.objects.create(customer=self.customer)
        self.product = Product.objects.create(name='Test Product', price=100, stock=10)

    def test_get_cart_items_success(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        url = reverse('cart-items', kwargs={'user_id': self.customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['quantity'], 2)

    def test_get_cart_items_not_found(self):
        url = reverse('cart-items', kwargs={'user_id': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Cart does not exist')

    def test_create_cart_item_success(self):
        url = reverse('cart-items', kwargs={'user_id': self.customer.id})
        data = {'product': self.product.id, 'quantity': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
