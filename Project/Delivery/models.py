from django.db import models
from Customer .models import Order
# Create your models here.
class Delivery(models.Model):
    delivery_id=models.IntegerField(blank=True,null=True)
    delivery_name=models.CharField(max_length=100)
    delivery_address=models.CharField(max_length=200)
    delivery_phone=models.IntegerField(blank=True, null=True,unique=True)

    #order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.delivery_name  