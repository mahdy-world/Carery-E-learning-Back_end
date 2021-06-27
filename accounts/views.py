from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from django.http.response import HttpResponseRedirect


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




def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        else:
            messages.success(request, 'بيانات الدخول خاطئة')

    return render(request, 'registration/login.html')
