# from django.shortcuts import render

# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Product
# from .serializers import ProductSerializer
# from customer.models import Customer

# Import Order model and OrderSerializer (assuming you have created a serializer for the Order model)
# @csrf_exempt
# def products(request):
#     if request.method == 'GET':
#         # Get a list of all the orders in the database
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         response_data = {'data': serializer.data}  # Add data property
#         return JsonResponse(response_data, safe=False)
#     elif request.method == 'POST':
#         # Add a new order to the database
#         # Assuming the request contains JSON data with 'item' and 'amount' fields
#         data = json.loads(request.body)
#         serializer = AddProductSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     else:
#         return JsonResponse({'error': 'Method not allowed'})
    
# @csrf_exempt
# def single_product(request, product_id):
#     try:
#         product = Product.objects.get(pk=product_id)
#     except product.DoesNotExist:
#         return JsonResponse({'error': 'Order does not exist'}, status=404)

#     if request.method == "GET":
#         # Get an individual order by its ID
#         serializer = Product(product)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         # Update an existing order with new information
#         # Assuming the request contains JSON data with 'item' and 'amount' fields
#         data = json.loads(request.body)
#         serializer = AddProductSerializer(product, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         # Remove an order from the database
#         product.delete()
#         return JsonResponse({'message': 'Order deleted successfully'}, status=204)

#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
