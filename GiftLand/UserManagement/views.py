from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import ProfileForm
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

@login_required
def create_profile(request) :
    form = ProfileForm()

    if request.method == "POST" :
        form = ProfileForm(request.FILES, request.POST)

        if form.is_valid() :
            pro_obj = form.save(commit=False)
            pro_obj.user = request.user

            pro_obj.save()

            return redirect('http://localhost:8000/')

    context = {
        'form' : form
    }
    return render(request, 'profile/create_profile.html', context)

def view_profile(request) :
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile' : profile,
    }
    return render(request, 'profile/view_profile.html', context)


