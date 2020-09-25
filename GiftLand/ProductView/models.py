from django.db import models

# Create your models here.
class Product(models.Model):
    p_id=models.IntegerField(default=0)
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField(default=0)
    totalstock=models.CharField(max_length=100,default='')
    p_image=models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.p_name  