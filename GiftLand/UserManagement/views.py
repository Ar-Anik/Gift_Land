from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import reg_forms

# Create your views here.


def Register(response):
    if response.method == 'POST':
        form = reg_forms(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = reg_forms()
    return render(response, 'register/register.html', {"form": form})
