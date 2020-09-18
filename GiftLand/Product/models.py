from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField(blank=True,null=True)
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField(blank=True,null=True)
    product_totalstock=models.CharField(max_length=100)


    def __str__(self):
        return self.product_name

class Category(models.Model):
    category_id=models.IntegerField(blank=True,null=True)
    category_type=models.CharField(max_length=200)

    product=models.ManyToManyField(Product)

    def __str__(self):
        return self.category_type        

class Review(models.Model):
    review_id=models.IntegerField(blank=True,null=True)
    review_rating=models.CharField(max_length=100)
    review_comment=models.CharField(max_length=200)
    
    product=models.ManyToManyField(Product)
    
    def __str__(self):
        return self.review_comment  

class Cart(models.Model):
    cart_id=models.IntegerField(blank=True,null=True)
    cart_status=models.CharField(max_length=100)
    cart_time=models.DateTimeField(auto_now_add=True)
    cart_discount=models.CharField(max_length=200)
    
    product=models.ManyToManyField(Product)
    
    def __str__(self):
        return self.cart_discount                