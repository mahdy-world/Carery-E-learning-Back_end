from django.db import models

GENDER = {
    ('ذكر','ذكر'),
    ('انثي','انثي'),
}

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30 , verbose_name="الاسم ")
    user_name = models.CharField(max_length=30  , verbose_name=" اسم المستخدم")
    password = models.CharField(max_length = 20 , verbose_name=" كلمة المرور")
    email = models.EmailField(  verbose_name="البريد الالكتروني")
    date_of_birth = models.DateField( verbose_name="تاريخ الميلاد")
    phone = models.CharField(max_length = 20 , verbose_name="رقم الموبيل")
    image = models.ImageField(  verbose_name="صورة البروفيل")
    facebook = models.CharField(max_length = 240 , verbose_name="الفيس بوك")
    instagram = models.CharField(max_length = 240 , verbose_name="الانستجرام")
    twitter = models.CharField(max_length = 240 , verbose_name="التويتر")
    linked_in = models.CharField(max_length = 240 , verbose_name="لينكدان")
    Gender = models.CharField(max_length=40, choices=GENDER , verbose_name="النوع")


class City (models.Model):
    
    name= models.CharField(max_length = 10)

class Govenorate (models.Model):

    name= models.CharField(max_length = 10)
    city = models.ForeignKey(City, on_delete=models.CASCADE )



