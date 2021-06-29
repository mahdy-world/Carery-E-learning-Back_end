from Courses.models import Course, CoursesRegistration, VedioUrl
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import *
from accounts.forms import *
from django.urls import reverse
from Book.models import Book
from Trainer.models import Trainer



# Create your views here.

def home(request):
    books=Book.objects.all().order_by('-created_in')[0:4]
    trainer=Trainer.objects.all()[0:4]
    course=Course.objects.all().order_by('-created_in')[0:4]
    student=Student.objects.all()
    vedio=VedioUrl.objects.all()
    feedback = Feedback.objects.all()
    
    return render(request, 'home.html', {'books':books,'trainer':trainer,'co':course , 'fee' : feedback, 'student':student, 'vedio':vedio})

@login_required()
def student(request):
    student = Student.objects.get(user=request.user)
    
    return render(request , 'profile.html' , {'student' : student})  

@login_required()
def edit_student(request):
    student = Student.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UserForm(request.POST , instance=request.user)
        studentform = StudentForm(request.POST , request.FILES , instance=student)
        
        if userform.is_valid() and studentform.is_valid():
            userform.save()
            mystudent = studentform.save(commit = False)
            mystudent.user = request.user
            mystudent.save()
            return redirect(reverse('Auth:student'))

    else:
        userform = UserForm(instance=request.user)
        studentform = StudentForm(instance=student)

    return render(request , 'edit_student.html' ,{'userform' : userform , 'studentform' : studentform})

@login_required()
def my_dashboard(request):
    myCuorses = CoursesRegistration.objects.filter(student_id=request.user.id)
    # all = myCuorses.Course.all()
    
   
    print(myCuorses)
    return render(request,'mydashboard.html' , {'myCuorses':myCuorses})