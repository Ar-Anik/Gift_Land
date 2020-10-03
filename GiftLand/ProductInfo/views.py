from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product
from .models import Order
from .models import Cart
from .forms import ProductForm
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

def ViewCart(request):
    cart = Cart.objects.get(user=request.user)

    total=0
    for i in cart.product.all():
        total+= i.p_price

    context={
        'cart':cart,
        'total':total,
    }

    return render (request,'ProductHtml/cart.html',context)  

@login_required
def AddtoCart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    cart.product.add(product)
    cart.save()

    return redirect('cart')  


@login_required
def RemovefromCart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)

    cart.product.remove(product)
    cart.save()

    return redirect('cart') 


@login_required
def CreateOrder(request) :
    
    orders = Order(user=request.user)

    try : 
        orders = Order.objects.filter(user=request.user)
        order_status = True
    except orders.DoesNotExist:
        orders = Order(user=request.user)
        order_status = False

    total = 0

    for i in orders :
        total += i.product.price

    context = {
        'orders' : orders,
        'order_status' : order_status,
        'total' : total
    }

    return render(request, 'ProductHtml/order.html', context)

@login_required
def UserOrder(request, product_id) :
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()

    return redirect('cart')

def Payment(request, product_id) :
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)

    order.transaction_id = request.POST['transaction_id']
    order.payment_options = 'Bkash'
    order.save()

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()

    return redirect('cart')

