"""GiftLand URL Configuration

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
from Product import views as Product_views
from Admin import views as Admin_views
from user import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', Product_views.Show_Product),
    path('add/', Product_views.ProductAdd),
    path('addcat/', Product_views.CategoryAdd),
    path('addre/', Product_views.ReviewAdd),
    path('addcart/', Product_views.CartAdd),
    path('manage/', Admin_views.Show_Admin),
    path('adda/', Admin_views.AdminAdd),
    path('addDelivery/', user_views.addDelivery),

]
