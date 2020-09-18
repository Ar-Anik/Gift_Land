from django.shortcuts import render
from .models import *
# Create your views here.
def Show_User(request):
    user_info=User.objects.all()
    order_info=Order.objects.all()
    delivery_info=Delivery.objects.all()
    payment_info=Payment.objects.all()
    context={
        'user_info':user_info,
        'order_info':order_info,
        'delivery_info':delivery_info,
        'payment_info':payment_info
    }
    return render(request,'user.html',context)

    
#def Show_Order(request):
    #order_info=Order.objects.all()
    #context={
     #   'order_info':order_info,
    #}
    #return render(request,'user.html',context)    