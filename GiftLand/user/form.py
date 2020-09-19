from django import forms
from .models import user
from .models import order
from .models import payment


class adduser(forms.ModelForm):
    class Meta:
        model=user
        fields = '__all__'

class addorder(forms.ModelForm):
    class Meta:
        model=order
        fields = '__all__'

class addpayment(forms.ModelForm):
    class Meta:
        model=payment
        fields = '__all__'
