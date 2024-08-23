from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User
from .serializers import CartDetailSerializer, CartSerializer
from .models import Cart, CartDetail
from product.models import Product

class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(id= self.kwargs['user_id']) to make this you have to change the urls to: path('api/<int:user_id>/cart', CartDetailCreateAPI.as_view()),
        user = User.objects.get(username= self.kwargs['username']) 
        cart,created = Cart.objects.get_or_create(user=user,status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})



    def post(self, request, *args, **kwargs):
        user = User.objects.get(username= self.kwargs['username']) 
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
        cart = Cart.objects.get(user=user,status='Inprogress')
        cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
        cart_detail.quantity = quantity
        cart_detail.total = round(quantity* product.price , 2)
        cart_detail.save()
        cart = Cart.objects.get(user=user,status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'message':'product is added successfully', 'cart':data})




    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username= self.kwargs['username']) 
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()
        cart = Cart.objects.get(user=user,status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'message':'product is deleted successfully', 'cart':data})