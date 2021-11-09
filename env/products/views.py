from django.shortcuts import get_object_or_404, render
from .models import Products
from category.models import Category
# Create your views here.
def products(request, category_slug=None):
    categories=None
    products=None

    if category_slug!=None:
        categories=get_object_or_404(Category, slug=category_slug)
        products=Products.objects.filter(model_category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Products.objects.all().filter(is_available=True)
        product_count=products.count()
    context={
            'products':products,
            'productCount':product_count,
    }
    return render(request,'products/products.html', context)

def productInfo(request, category_slug,product_slug):
    try:
        singleproduct=Products.objects.get(model_category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={
        'singleproduct':singleproduct,
    }
    return render(request,'products/productInfo.html',context)