from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CartView, CartItemView

urlpatterns = [
    path('<int:user_id>/', CartView.as_view(), name='cart'),
    path('<int:user_id>/items/', CartItemView.as_view(), name='cart-items'),
]
