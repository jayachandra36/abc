from rest_framework import serializers
from .models import Register, Product

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ("id",
                  "user_name",
                  "password",
                  "email_id",
                  "mobile_number")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id",
                  "product_name",
                  "product_cost",
                  "product_type",
                  "product_description")
