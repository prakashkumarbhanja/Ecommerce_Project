from django.shortcuts import render
from django.views.generic.detail import DetailView


from .models import *

# Create your views here.

def home(request): #16
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products/home.html', context)

class ProductDetail(DetailView):
    model = Product

def search(request): #21 venv\Scripts\activate
    try:
        q = request.GET.get('q')
    except:
        q=None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'q': q, 'products': products}
        template = 'products/result.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)
