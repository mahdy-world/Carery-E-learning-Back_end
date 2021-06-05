from django.shortcuts import redirect, render
from .models import * 


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
    if Student.objects.filter(id=request.user.id):
        user = Student.objects.get(id=request.user.id)
    else:
        user = None
    user_course = CoursesRegistration.objects.filter(student=user, course=course)
    user_count = CoursesRegistration.objects.filter(course=course)
    videos =  VedioUrl.objects.filter(course=course)

    return render(request , 'courses/course_details.html',{'da':course, 'user_course':user_course ,'user_count':user_count , 'videos':videos})  



def course_contante(request,pk):
    vedio = VedioUrl.objects.filter(course_id=pk).order_by('id')
    course = Course.objects.get(id=pk)
    return render(request , 'courses/course_contante.html',{'dv':vedio , 'co' : course}) 



def video_content(request, id):
    video = VedioUrl.objects.get(id=id)
    video.shows += 1
    video.save()
    vedio = VedioUrl.objects.filter(course_id=video.course.id).order_by('id')
    course = Course.objects.get(id=video.course.id)
    return render(request , 'courses/course_contante.html',{'dv':vedio , 'co' : course, 'video':video}) 



def enroll_courses(request, pk):
    vedio = VedioUrl.objects.filter(course_id=pk).order_by('id')
    course = Course.objects.get(id=pk)

    user = Student.objects.get(user=request.user)

    registeration = CoursesRegistration()
    registeration.student = user
    registeration.course = Course.objects.get(id=pk)

    registeration.save()

    return render(request,'courses/course_contante.html',{'dv':vedio , 'co' : course})
    