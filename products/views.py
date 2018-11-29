from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products" : products})
    

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    currency = request.session.get("currency", "EUR")
    return render(request, "products/product_detail.html", {"product" : product, "currency": currency})
    
    
def homepage(request):
    return render(request, "homepage.html")    

