from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_debug
from .api import ProductListAPI , ProductDetailAPI , BrandListAPI , BrandDetailAPI

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',queryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),

    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),

    # API 
    path('api/list',ProductListAPI.as_view()),
    path('api/list/<int:pk>',ProductDetailAPI.as_view()),
    path('brands/api/list',BrandListAPI.as_view()),
    path('brands/api/list/<int:pk>',BrandDetailAPI.as_view()),
]
