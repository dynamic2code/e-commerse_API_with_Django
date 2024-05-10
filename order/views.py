import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from customer.models import Customer
from .sms import sending

class OrdersView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            customer_id = request.data.get('customer_id')
            if customer_id:
                try:
                    customer = Customer.objects.get(pk=customer_id)
                    order = serializer.save(customer=customer)
                    sending(order.phone_number)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Customer.DoesNotExist:
                    return Response({'error': 'Invalid customer ID'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Missing customer ID'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleOrderView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, order_id):
        try:
            return Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return None

    def get(self, request, order_id):
        order = self.get_object(order_id)
        if order:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        return Response({'error': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, order_id):
        order = self.get_object(order_id)
        if order:
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, order_id):
        order = self.get_object(order_id)
        if order:
            order.delete()
            return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)
