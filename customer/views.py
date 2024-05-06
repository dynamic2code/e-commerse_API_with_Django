from django.shortcuts import render,redirect
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
                    token = jwt.encode(payload, settings.SECRET_KEY , algorithm='HS256')
                    return JsonResponse({'token': token}, status=200)
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
    