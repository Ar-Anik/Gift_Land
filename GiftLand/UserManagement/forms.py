from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = ('Picture_Picture', 'contact_num', 'address')


