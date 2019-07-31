from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detial_view(request):
    obj = Product.objects.get(id=1)
    '''context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
    }'''
    context = {
        'object': obj
    }
    return render(request, "products/products_detail.html", context)
