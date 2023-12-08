from rest_framework import serializers
from .models import Product , Brand , Review
from django.db.models.aggregates import Avg 




class ProductListSerializer(serializers.ModelSerializer):
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



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    reviews = ReviewSerializer(source='review_product',many=True)

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



class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'
