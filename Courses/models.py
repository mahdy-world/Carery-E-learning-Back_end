from django.db import models
from accounts.models import Student
from Book.models import Category
from Trainer.models import Trainer
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'اسم الكورس' )
    image= models.ImageField(upload_to='courses/', verbose_name='صورة الكورس')
    detail_image= models.ImageField(upload_to='courses/', verbose_name='صورة الوصف')
    price = models.CharField(max_length=10, verbose_name='السعر')
    duration = models.CharField( max_length=10 , verbose_name = 'مدة الكورس')
    count_lesson = models.CharField(max_length=100 , verbose_name='عدد الدروس')
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category,related_name = "course_category" ,on_delete=models.CASCADE , verbose_name = 'قسم الكورس')
    trainer = models.ForeignKey(Trainer,related_name = "Trainer_name" ,on_delete=models.CASCADE , verbose_name = 'اسم المدرب')
    
    
    def __str__(self):
        return self.name

class CoursesRegistration(models.Model):
    student = models.ForeignKey(Student, related_name="student_register", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="course_register", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.first_name


class VedioUrl(models.Model):
    course = models.ForeignKey(Course,related_name="vedio_courses", on_delete=models.CASCADE , verbose_name = 'الكورس')
    title = models.CharField(max_length=100, verbose_name = 'عنوان الفيديو')
    url = models.CharField(max_length=500,verbose_name = 'رابط الفيديو')
    

    def __str__(self):
        return self.title
    
    


