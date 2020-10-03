from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
def ShowProducts(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'ProductHtml/index.html', context)


def ProductDetails(request, product_id):
    detail = get_object_or_404(Product, id=product_id)
    context = {
        'detail': detail,
    }
    return render(request, 'ProductHtml/productdetail.html', context)
