from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from product.models import Product
from customer.models import Customer


class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"sms {self.phone_number}"

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.product} in {self.order.customer.username}'s order"
