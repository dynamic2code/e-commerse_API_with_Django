from django.utils import timezone
from django.db import models
from customer.models import Customer
# Create your models here.

class Order(models.Model):
    order_id =  models.AutoField(primary_key=True)
    item = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    time = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   