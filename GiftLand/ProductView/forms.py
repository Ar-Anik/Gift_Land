from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'category', 'p_price', 'p_image', 'description')
