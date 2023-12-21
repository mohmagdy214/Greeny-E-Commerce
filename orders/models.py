from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils import timezone

# Create your models here.

CART_STATUS = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=10,choices=CART_STATUS)


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    qunatity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)


ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=10,choices=ORDER_STATUS)
    code = models.CharField(max_length=10)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField()
    qunatity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)


class Coupon(models.Model):
    pass