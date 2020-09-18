from django.shortcuts import render
from .models import *
# Create your views here.
def Show_Delivery(request):
    delivery_info=Delivery.objects.all()
    context={
        'delivery_info':delivery_info,
    }
    return render(request,'delivery.html',context)