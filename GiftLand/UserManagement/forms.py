from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

#class ProfileForm(forms.ModelForm) :
    #class Meta:
        #model = Profile
        #fields = ('Picture_Picture', 'contact_num', 'address')


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('name','Picture_Picture','Phone') 