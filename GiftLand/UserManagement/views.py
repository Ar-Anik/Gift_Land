from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

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





#def Register(response):
    #if response.method == 'POST':
        #form = reg_forms(response.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('login')
    #else:
        #form = reg_forms()
    #return render(response, 'registration/register.html', {"form": form})
