from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()

    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'index.html', {'products': products})