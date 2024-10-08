from django.urls import path
from .views import OrderList , checkout , add_to_cart , remove_from_cart
from .api import CartDetailCreateAPI


app_name = 'orders'


urlpatterns = [
    path('' , OrderList.as_view()),
    path('checkout' , checkout),
    path('add-to-cart' , add_to_cart , name='add_to_cart'),
    path('<int:product_id>/remove-from-cart' , remove_from_cart),


    #api
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),
]

