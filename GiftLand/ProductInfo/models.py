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

class Order(models.Model) :
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    status = models.CharField(max_length=200, choices=STATUS_CHOICES, blank=True)
    
    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Cash on Delivery', 'Cash on Delivery')
    )

    payment_options = models.CharField(max_length=200, choices=PAYMENT_CHOICES, default='Bkash')
    paid_status = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username + " " + self.product.name + " " + self.status   