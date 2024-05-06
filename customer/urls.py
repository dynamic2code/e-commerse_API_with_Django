from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    customer,
    sign_up,
    login
) 

urlpatterns = [
    path('/sign_up', sign_up , name='sign_up'),
    path('/log_in', login, name='sign_up'),
    path('', customer, name='customer')
]
