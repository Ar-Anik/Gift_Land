from django.db import models
from Product .models import Product
from Product .models import Cart
# Create your models here.
class User(models.Model):
    User_Id=models.IntegerField(blank=True,null=True)
    User_name=models.CharField(max_length=100)
    User_email=models.CharField(max_length=200,unique=True)
    User_password=models.CharField(max_length=100)
    User_address=models.CharField(max_length=200)
    User_phone=models.IntegerField(blank=True,null=True,unique=True)

    Product=models.ManyToManyField(Product)
    Cart=models.ForeignKey(Cart,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.User_name


class Order(models.Model):
    order_id=models.IntegerField(blank=True,null=True)
    order_status=models.CharField(max_length=200)
    order_date=models.DateTimeField(auto_now_add=True)
    
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)  
    Cart=models.ForeignKey(Cart,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.order_status

class Delivery(models.Model):
    delivery_id=models.IntegerField(blank=True,null=True)
    delivery_name=models.CharField(max_length=100)
    delivery_address=models.CharField(max_length=200)
    delivery_phone=models.IntegerField(blank=True, null=True,unique=True)

    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.delivery_name                


class Payment(models.Model):
    payment_id=models.IntegerField(blank=True,null=True)
    payment_type=models.CharField(max_length=100)
    payment_amount=models.IntegerField(blank=True,null=True)

    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.payment_type        