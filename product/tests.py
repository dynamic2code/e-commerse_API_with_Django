from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
import tempfile

class ProductTests(APITestCase):
    def setUp(self):
        # Prepare test image
        test_image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        
        # Create test products
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', price=100, stock=10, image=test_image)
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', price=200, stock=20)

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if all products are returned

    def test_create_product_without_image(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 150, 'stock': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_product_detail(self):
        url = reverse('product-detail', args=[self.product1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

    def test_delete_product(self):
        url = reverse('product-detail', args=[self.product1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)