# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductListSerializer , ProductDetailSerializer , BrandListSerializer , BrandDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .myfilters import ProductFilter
from .mypagination import MyPagination
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
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag' ,'brand']
    search_fields = ['name' ,'subtitle' ,'description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]



class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]



class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer



class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer