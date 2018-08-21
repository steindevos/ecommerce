from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product

# Create your views here.
def show_products(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {'products': products})
    
def show_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_details.html", {'product': product})