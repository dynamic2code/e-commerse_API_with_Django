from rest_framework import serializers
from .models import Customer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.hashers import make_password

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )

    class Meta:
        model = Customer
        fields = ('username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        customer = Customer.objects.create(**validated_data)
        return customer
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Perform additional validation if needed
        if not email:
            raise serializers.ValidationError("Email is required")
        if not password:
            raise serializers.ValidationError("Password is required")

        return data


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'username', 'email','phone_number']
