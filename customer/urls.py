from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    customer,
    sign_up,
    login,
    login_openId
) 

urlpatterns = [
    path('/sign_up', sign_up , name='sign_up'),
    path('/login_openId', login_openId, name='login_openId'),
    path('/log_in', login, name='log_in'),
    path('', customer, name='customer')
]
