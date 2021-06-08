from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *


# Create your views here.
def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'registration/sign_up.html',{'form':form})