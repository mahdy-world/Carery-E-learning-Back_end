from django.shortcuts import render
from .models import * 


# Create your views here.
def category_list(request):
    return render(request ,'category.html')

def programming_list(request):
    queryset = Course.objects.filter(category__id = 1)
    print(queryset)
    return render(request , 'programming.html' ,{'course' : queryset} )

def course_detail (request,pk):
    course = Course.objects.get(id=pk)
    return render(request , 'course_details.html',{'da':course})  

# def course_contante(request,pk):  
#     course = Course.objects.get(id=pk)
#     return render(request , 'course_details.html',{'da':course})