from django.contrib import messages
from django.http.response import HttpResponseRedirect
from Courses.forms import RateForm
from django.shortcuts import redirect, render
from .models import * 
from .forms import RateForm
from django.db.models import Avg

# Create your views here.
def category_list(request):
    return render(request ,'category/category.html')

def programming_list(request):
    queryset = Course.objects.filter(category__id = 1)
    return render(request , 'category/programming.html' ,{'course' : queryset} )


def design_list(request):
    queryset = Course.objects.filter(category__id = 2)
    return render(request , 'category/design.html' ,{'course' : queryset} )


def lang_list(request):
    queryset = Course.objects.filter(category__id = 3)
    return render(request , 'category/lang.html' ,{'course' : queryset} )


def database_list(request):
    queryset = Course.objects.filter(category__id = 4)
    return render(request , 'category/database.html' ,{'course' : queryset} )


def network_list(request):
    queryset = Course.objects.filter(category__id = 5)
    return render(request , 'category/network.html' ,{'course' : queryset} )


def development_list(request):
    queryset = Course.objects.filter(category__id = 6)
    return render(request , 'category/development.html' ,{'course' : queryset} )


def system_list(request):
    queryset = Course.objects.filter(category__id = 7)
    return render(request , 'category/system.html' ,{'course' : queryset} )


def secuirty_list(request):
    queryset = Course.objects.filter(category__id = 8)
    return render(request , 'category/secuirty.html' ,{'course' : queryset} )


def course_detail (request,pk):
    course = Course.objects.get(id=pk)
   
    return render(request , 'courses/course_details.html',{'da':course })  



def course_contante(request,pk):
    vedio = VedioUrl.objects.filter(course_id=pk).order_by('id')
    course = Course.objects.get(id=pk)
    reviwes = Review.objects.filter(course=course)
    reviwes_avg = reviwes.aggregate(Avg('rate'))
    reviwes_count = reviwes.count()
   
    
    return render(request , 'courses/course_contante.html',{'dv':vedio , 'co' : course,'avg':reviwes_avg,'count':reviwes_count}) 


def rate (request,pk):
    
    course = Course.objects.get(id=pk)
    user = Student.objects.get(id=request.user.id)
    
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.course = course
            rate.student = user
            rate.save()
            
            messages.success(request, 'تم الارسال بنجاح')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    else :
            
        form =RateForm()
    
    
    return render (request , 'courses/rate.html', {'co' : course,'form': form})