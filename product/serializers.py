from rest_framework import serializers
from .models import Product , Brand
from django.db.models.aggregates import Avg 




class BrandListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'




class ProductListSerialzer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    
    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews




class ProductDetailSerialzer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    
    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews 




class BrandDetailSerialzer(serializers.ModelSerializer):
    products = ProductListSerialzer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'