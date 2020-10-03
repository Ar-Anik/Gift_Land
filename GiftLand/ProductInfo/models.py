from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    p_id=models.IntegerField(default=0)
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField(blank=True)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)
    p_image=models.ImageField(upload_to='product/images')
    #file = models.FileField(upload_to='products/files/', blank=True, null=True, default='products/files/default.pdf')
    
    def __str__(self):
        return self.p_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ManyToManyField(Product)


    created_date= models.DateTimeField(auto_now_add= True ,auto_now=False)
    update_date=models.DateTimeField(auto_now_add=False ,auto_now=True)

    def __str__(self):
        return self.user.username        