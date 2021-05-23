from django.shortcuts import redirect, render
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم الارسال بنجاح')
    
    form = ContactForm()
    return render(request , 'contact.html' , {'form': form})
            