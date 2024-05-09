from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.signals import user_logged_in
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

import requests
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
from .serializer import SignUpSerializer, LoginSerializer, CustomerSerializer
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.permissions import AllowAny 
import jwt
from django.conf import settings

class GoogleLogin(SocialLoginView):
    """Google login"""
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_CALLBACK_URL
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
        return response
    
class GoogleCallback(APIView):
    """Google callback"""
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code:
            res = requests.post(
                "https://accounts.google.com/o/oauth2/token",
                params={
                    "client_id": settings.CLIENT_ID,
                    "client_secret": settings.CLIENT_SECRET,
                    "redirect_uri": request.build_absolute_uri(reverse("google_callback")),
                    "grant_type": "authorization_code",
                    "code": code,
                },
            )
            res = requests.post(
                request.build_absolute_uri(reverse("google_login")),
                data={"access_token": res.json()["access_token"]},
            )
            return redirect('http://localhost:5173/feed')
        return JsonResponse({"error": "Access denied"}, status= 403)


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print (data)
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                customer = Customer.objects.get(email=email)
                # Check if the password matches
                if check_password(password, customer.password):
                    payload = {
                        'user_id': customer.customer_id,
                        'name': customer.username,
                    }
                    user = payload 
                    token = jwt.encode(payload, settings.SECRET_KEY , algorithm='HS256')
                    return JsonResponse({'token': token, 'user':user}, status=200)
                else:
                    # Password is incorrect
                    return JsonResponse({'error': 'Invalid email or password'}, status=400)
            except Customer.DoesNotExist:
                # Customer does not exist
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
        else:
            # Invalid serializer data
            return JsonResponse(serializer.errors, status=400)
    else:
        # Method not allowed
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def customer(request):
    if request.method == 'GET':
        # Get a list of all the orders in the database
        orders = Customer.objects.all()
        serializer = CustomerSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'})
    