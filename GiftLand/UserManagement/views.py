# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.forms import ModelForm
# from .forms import ProfileForm
# from .models import Profile

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import Profileform
from .models import Profile

# Create your views here.

def Registerpage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    
    context={
        'form':form,
    }
    return render(request,'registration/register.html',context) 

# @login_required
# def Createprofile(request) :
#     form = ProfileForm()

#     if request.method == "POST" :
#         form = ProfileForm(request.FILES, request.POST)

#         if form.is_valid() :
#             pro_obj = form.save(commit=False)
#             pro_obj.user = request.user

#             pro_obj.save()

#             return redirect('http://localhost:8000/')

#     context = {
#         'form' : form
#     }
#     return render(request, 'UserManagement/create_profile.html', context)

#def Viewprofile(request) :
    #profile=Profile.objects.get(user=request.user)
    #context = {
        #'profile':profile,
    #}
    #return render(request, 'UserManagement/view_profile.html', context)

@login_required
def CreateProfile(request):
    form = Profileform()
    if request.method == "POST":
        form = Profileform(request.POST,request.FILES)
    if form.is_valid():
        profile_object =form.save(commit=False)
        profile_object.user =request.user
        profile_object.save()
        return redirect('/')
    context ={
        'form':form,
    }
    return render(request,'UserManagement/create_profile.html',context)    



def ViewProfile(request):
    profile=Profile.objects.get(user=request.user)    
    context ={
        'profile':profile,
    }
    return render(request,'UserManagement/view_profile.html',context)
