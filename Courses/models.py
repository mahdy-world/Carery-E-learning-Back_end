from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from accounts.models import Student
from Book.models import Category
from Trainer.models import Trainer
# Create your models here.
  
class Sponsers(models.Model):
    name = models.CharField(max_length = 150 , verbose_name='الاسم')
    address = models.CharField(max_length = 150 , verbose_name='العنوان')
    phone = models.CharField(max_length = 150 , verbose_name='رقم الموبيل')
    logo= models.ImageField(upload_to='sponsers/', verbose_name='الشعار')
    
    def __str__(self):
        return self.name

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
    
    title1 = models.CharField(max_length=50 , null=True , verbose_name='العنوان الاول')
    p1 = models.CharField(max_length=100 , null=True , verbose_name='العنوان الفرعي الاول')
    image1 = models.ImageField(upload_to='summary/', null=True , verbose_name='الصورة الاولي' )
    
    title2 = models.CharField(max_length=50 , null=True , verbose_name='العنوان الثاني')
    p2 = models.CharField(max_length=100 , null=True , verbose_name='العنوان الفرعي الثاني')
    image2 = models.ImageField(upload_to='summary/', null=True , verbose_name='الصورة الثانية' )
    
    title3 = models.CharField(max_length=50 , null=True , verbose_name='العنوان الثالث')
    p3 = models.CharField(max_length=100 ,  null=True ,verbose_name='العنوان الفرعي الثالث')
    image3 = models.ImageField(upload_to='summary/', null=True , verbose_name='الصورة الثالثة' )

    title4 = models.CharField(max_length=50 , null=True , verbose_name='العنوان الرابع')
    p4 = models.CharField(max_length=100 , null=True ,verbose_name='العنوان الفرعي الرابع')
    image4 = models.ImageField(upload_to='summary/', null=True , verbose_name='الصورة الرابعة' )

    title5 = models.CharField(max_length=50 , null=True , verbose_name='العنوان الخامس')
    p5 = models.CharField(max_length=100 ,  null=True ,verbose_name='العنوان الفرعي الخامس')
    image5 = models.ImageField(upload_to='summary/', null=True , verbose_name='الصورة الخامسة' )
    
    sponsers = models.ForeignKey(Sponsers, null=True, related_name="course_sponsers" ,on_delete=models.CASCADE, verbose_name='الرعاة')
     
    
    def __str__(self):
        return self.name



class CoursesRegistration(models.Model):
    student = models.ForeignKey(Student, related_name="student_register", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="course_register", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.username


class VedioUrl(models.Model):
    course = models.ForeignKey(Course,related_name="vedio_courses", on_delete=models.CASCADE , verbose_name = 'الكورس')
    title = models.CharField(max_length=100, verbose_name = 'عنوان الفيديو')
    url = models.CharField(max_length=500,verbose_name = 'رابط الفيديو')
    shows = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
    

    
    
    
        
    
 
  