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
from django.urls import path, include
from django.conf.urls.static import static
from Product import views as Product_views
from Admin import views as Admin_views
from user import views as user_views
from ProductInfo import views as Product
from UserManagement import views as userman_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', Product_views.Show_Product),
    path('addproduct/', Product_views.ProductAdd),
    path('addcategory/', Product_views.CategoryAdd),
    path('addreview/', Product_views.ReviewAdd),
    path('addcart/', Product_views.CartAdd),
    path('manage/', Admin_views.Show_Admin),
    path('adda/', Admin_views.AdminAdd),
    path('user', user_views.customer),
    path('adduser/', user_views.useradd),
    path('addorder/', user_views.orderadd),
    path('addpayment/', user_views.paymentadd),
    path('adddelivery/', user_views.addDelivery),
    path('signup/', userman_views.Registerpage),
    # path('createprofile/', userman_views.Createprofile, name='createprofile'),
    # path('viewprofile/', userman_views.Viewprofile, name='viewprofile'),
    path('profile/', userman_views.CreateProfile),
    path('profileview/', userman_views.ViewProfile),
    path('', Product.ShowProducts),
    path('account/', include('django.contrib.auth.urls')),
    path('<int:product_id>', Product.ProductDetails),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
