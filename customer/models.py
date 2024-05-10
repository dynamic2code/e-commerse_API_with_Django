from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',  # New argument
        blank=True,
        help_text='The groups this customer belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_permissions',  # New argument
        blank=True,
        help_text='Specific permissions for this customer.'
    )
