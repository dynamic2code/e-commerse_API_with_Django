from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import OrdersView, SingleOrderView

urlpatterns = [
    path('', OrdersView.as_view(), name='orders'),
    path('<int:order_id>/', SingleOrderView.as_view(), name='single_order'),
]
