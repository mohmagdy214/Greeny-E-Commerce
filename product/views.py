from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Review
from django.db.models import Q , F , Value
from django.db.models.aggregates import Min , Max , Count , Avg , Sum
# Create your views here.

def queryset_debug(request):
    # queryset_api_methods

    data = Product.objects.select_related('brand').all()              # prefetch_related = many-to-many
    # data = Product.objects.filter(price__gt = 100)                 # greater than
    # data = Product.objects.filter(price__gte = 100)               # greater than or equal
    # data = Product.objects.filter(price__lt = 100)                 # less than 
    # data = Product.objects.filter(price__lte = 100)                 # less than or equal
    # data = Product.objects.filter(price__range = (990.16,1000))       # range

    #navigate relation
    # data = Product.objects.filter(brand__name = 'Kyle Butler')
    # data = Product.objects.filter(brand__price__gt = 100)

    #filter with text
    # data = Product.objects.filter(name__contains = 'Brown')
    # data = Product.objects.filter(name__startswith = 'Hailey')
    # data = Product.objects.filter(name__endswith = 'Brown')
    # data = Product.objects.filter(tags__isnull = True)
    # data = Review.objects.filter(created_at__year = 2023)
    # data = Review.objects.filter(created_at__month = 11)

    #filter 2 values
    # data = Product.objects.filter(price__gt = 990.16 , quantity__lt = 10) # and
    # data = Product.objects.filter(
    #     Q(price__gt = 990.16) |
    #     Q(quantity__lt = 10)
    # ) # or

    # data = Product.objects.filter(
    #     Q(price__gt = 990.16) &
    #     Q(quantity__lt = 10)
    # ) # and

    # data = Product.objects.filter(
    #     Q(price__gt = 990.16) &
    #     ~ Q(quantity__lt = 10)
    # ) # and not

    #field lookup
    # data = Product.objects.filter(price=F('quantity')) 

    # data = Product.objects.all().order_by('name')
    # data = Product.objects.all().order_by('-name')
    # data = Product.objects.all().order_by('name').reverse()
    # data = Product.objects.all().order_by('name','quantity')
    # data = Product.objects.all().order_by('name','-quantity')
    # data = Product.objects.all().earliest('name')  # first 
    # data = Product.objects.all().latest('name')  # last

    #slice
    # data = Product.objects.all()[10:20]

    #select columns
    # data = Product.objects.values('name','price','brand__name')
    # data = Product.objects.values_list('name','price','brand__name')

    # remove duplicate
    # data = Product.objects.all().distinct()
    # data = Product.objects.all().only('name','price')
    # data = Product.objects.all().defer('slug','description')

    #aggregation
    # data = Product.objects.aggregate(Sum('quantity'))
    # data = Product.objects.aggregate(Avg('price'))

    #annotate
    # data = Product.objects.annotate(is_new=Value(True))
    # data = Product.objects.annotate(price_with_tax=F('price')*1.5)

    return render(request , 'product/debug.html' , {'data':data})





class ProductList(ListView):
    model = Product    #context = product_list - object_list
    paginate_by = 20



class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context






class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20





class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug']) # overide query
        return super().get_queryset().filter(brand=brand) # Product query->(product.brand=brand*this one up*) 


    # retrieve new data : template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    

    # def brand_list(request):
    #     brands = Brand.objects.all()   # queryset : query db
    #     context = {'data':brands}   # context v:t
    #     return render(request , 'brands.html' , context)