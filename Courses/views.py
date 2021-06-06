from django.contrib import messages
from django.http.response import HttpResponseRedirect
from Courses.forms import RateForm
from django.shortcuts import redirect, render
from .models import * 
from .forms import RateForm
from django.db.models import Avg

# Create your views here.
def category_list(request):
    
    return render(request ,'category/category.html',)

def programming_list(request):
    queryset = Course.objects.filter(category__id = 1)
    

    user_count = CoursesRegistration.objects.filter(course=queryset)
    
    return render(request , 'category/programming.html' ,{'course' : queryset,'user_count':user_count } )


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
    
    if Student.objects.filter(id=request.user.id):
        user = Student.objects.get(id=request.user.id)
    else:
        user = None
    user_course = CoursesRegistration.objects.filter(student=user, course=course)
    user_count = CoursesRegistration.objects.filter(course=course)
    
    
    
    videos =  VedioUrl.objects.filter(course=course)
    
    reviwes = Review.objects.filter(course=course)
    reviwes_avg = reviwes.aggregate(Avg('rate'))
    

    return render(request , 'courses/course_details.html',{'da':course, 'user_course':user_course ,'user_count':user_count , 'videos':videos, 'avg':reviwes_avg})  


def course_contante(request,pk):
   
    vedio = VedioUrl.objects.filter(course_id=pk).order_by('id')
    course = Course.objects.get(id=pk)
    reviwes = Review.objects.filter(course=course)
    reviwes_avg = reviwes.aggregate(Avg('rate'))
    reviwes_count = reviwes.count()
   
    
    return render(request , 'courses/course_contante.html',{'dv':vedio , 'co' : course,'avg':reviwes_avg,'count':reviwes_count}) 


def video_content(request, id):
    video = VedioUrl.objects.get(id=id)
    video.shows += 1
    video.save()
    vedio = VedioUrl.objects.filter(course_id=video.course.id).order_by('id')
    course = Course.objects.get(id=video.course.id)
    return render(request , 'courses/course_contante.html',{'dv':vedio , 'co' : course, 'video':video})


def enroll_courses(request, pk):
     
    course = Course.objects.get(id=pk)
    course.student_count += 1
    course.save()  
        
    vedio = VedioUrl.objects.filter(course_id=pk).order_by('id')
    course = Course.objects.get(id=pk)

    user = Student.objects.get(user=request.user)

    registeration = CoursesRegistration()
    registeration.student = user
    registeration.course = Course.objects.get(id=pk)

    registeration.save()

    return render(request,'courses/course_contante.html',{'dv':vedio , 'co' : course})

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
    
    
    return render (request , 'courses/rate.html' , {'co' : course,'form': form})