from django.shortcuts import render
from .models import Admin
# Create your views here.
def Show_Admin(request):
    admin_info=Admin.objects.all()
    context={
        'admin_info':admin_info,
    }
    return render(request,'admin.html',context) 