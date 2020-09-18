"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Customer import views as Show_views
from Product import views as Product_views
from Admin import views as Admin_views
from Delivery import views as Delivery_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',Show_views.Show_User),
    path('product/',Product_views.Show_Product),
    path('manage/',Admin_views.Show_Admin),
    path('delivery/',Delivery_views.Show_Delivery)
]
