from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Review
# Create your views here.

def queryset_debug(request):
    data = Product.objects.all()
    return render(request , 'product/debug.html' , {'data':data})





class ProductList(ListView):
    model = Product    #context = product_list - object_list



class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context



class BrandList(ListView):
    model = Brand



class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand) # Product query->(product.brand=brand*this one up*) 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    