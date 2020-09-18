from django.shortcuts import render
from .models import *
# Create your views here.
def Show_Product(request):
    product_info=Product.objects.all()
    category_info=Category.objects.all()
    review_info=Review.objects.all()
    cart_info=Cart.objects.all()
    context={
        'product_info':product_info,
        'category_info':category_info,
        'review_info':review_info,
        'cart_info':cart_info,
    }
    return render(request,'product.html',context)