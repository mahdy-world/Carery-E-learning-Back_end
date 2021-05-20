from django.shortcuts import render
from .models import *

# Create your views here.


def all_tranier(request):
     tranier = Trainer.objects.all()
     context = {
         'all' : tranier
     }
     return render(request , 'list.html' , context)  
    
