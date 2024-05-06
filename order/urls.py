from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    orders,
    single_order
)

urlpatterns = [
    path('', orders, name='orders'),
    path('/<int:order_id>', single_order, name= 'single-order'),
]
