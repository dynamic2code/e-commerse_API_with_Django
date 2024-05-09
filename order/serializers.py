from rest_framework import serializers
from .models import Order, OrderItem
from customer.models import Customer
from product.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer')
    product_items = OrderItemSerializer(many=True, source='orderitem_set', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'amount', 'created_at', 'updated_at', 'customer_id', 'phone_number', 'product_items']

    def create(self, validated_data):
        products_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            OrderItem.objects.create(order=order, **product_data)
        return order
        