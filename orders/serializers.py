from rest_framework import serializers
from .models import Cart, CartDetail, Order, OrderDetail
# from product.serializers import ProductDetailSerializer


class CartDetailSerializer(serializers.ModelSerializer):
    # product = ProductDetailSerializer()
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'