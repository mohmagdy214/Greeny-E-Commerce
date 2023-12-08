# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductListSerialzer , ProductDetailSerialzer , BrandListSerialzer , BrandDetailSerialzer
from .models import Product , Brand
from rest_framework import generics



# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:20] # list
#     data = ProductSerialzer(products,many=True,context={'request':request}).data # json
#     return Response({'products':data})



# @api_view(['GET'])
# def product_detail_api(request,product_id):
#     product = Product.objects.get(id=product_id) 
#     data = ProductSerialzer(product,context={'request':request}).data # json
#     return Response({'product':data})




class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerialzer



class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerialzer



class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerialzer



class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerialzer