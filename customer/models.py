from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username  = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    email = models.EmailField(unique=True, verbose_name='Email address')
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=10)
