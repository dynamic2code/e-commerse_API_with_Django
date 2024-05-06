import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer
from customer.models import Customer
from .sms import sending
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Import Order model and OrderSerializer (assuming you have created a serializer for the Order model)
@csrf_exempt
def orders(request):
    if request.method == 'GET':
        # Get a list of all the orders in the database
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        response_data = {'data': serializer.data}  # Add data property
        return JsonResponse(response_data, safe=False)
    elif request.method == 'POST':
        # Add a new order to the database
        # Assuming the request contains JSON data with 'item' and 'amount' fields
        data = json.loads(request.body)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            customer_id = data.get('customer_id')  # Get customer ID from request body
            if customer_id:
                try:
                    customer = Customer.objects.get(pk=customer_id)
                    serializer.save(customer=customer)  # Save order with customer
                    numbers = list(customer.phone_number)  # Assuming phone_number is a field
                    sending(numbers)  # Trigger sending function (assumed)
                    return JsonResponse(serializer.data, status=201)
                except Customer.DoesNotExist:
                    return JsonResponse({'error': 'Invalid customer ID'}, status=400)
            else:
                return JsonResponse({'error': 'Missing customer ID'}, status=400)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'})
    
@csrf_exempt
def single_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order does not exist'}, status=404)

    if request.method == "GET":
        # Get an individual order by its ID
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        # Update an existing order with new information
        # Assuming the request contains JSON data with 'item' and 'amount' fields
        data = json.loads(request.body)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        # Remove an order from the database
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'}, status=204)

    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
