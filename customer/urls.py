from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    customer,
    sign_up,
    login,
    GoogleCallback,
    GoogleLogin
)

urlpatterns = [
    path('sign_up/', sign_up , name='sign_up'),
    path('log_in/', login, name='log_in'),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("google_callback/", GoogleCallback.as_view(), name="google_callback"),
    path('', customer, name='customer')
]
