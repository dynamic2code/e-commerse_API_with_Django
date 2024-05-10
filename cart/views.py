from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from product.models import Product
from customer.models import Customer
from .serializers import CartSerializer, CartItemSerializer

class CartView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, user_id):
        try:
            cart = Cart.objects.get(customer_id=user_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        try:
            customer = Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.save(customer=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, user_id):
        try:
            cart = Cart.objects.get(customer_id=user_id)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

        items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        try:
            cart = Cart.objects.get(customer=user_id)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = request.data.get('product')
            quantity = request.data.get('quantity', 1)
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
