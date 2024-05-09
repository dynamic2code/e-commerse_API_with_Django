from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product
from customer.models import Customer

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.username}'s cart"


class CartItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in {self.cart.customer.username}'s cart"
    