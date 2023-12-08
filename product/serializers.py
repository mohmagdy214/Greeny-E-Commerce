from rest_framework import serializers
from .models import Product , Brand



class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class BrandListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerialzer(serializers.ModelSerializer):
    products = ProductSerialzer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'