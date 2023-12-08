from rest_framework import serializers
from .models import Product , Brand



class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class BrandSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'