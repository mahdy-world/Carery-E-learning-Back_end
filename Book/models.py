from django.db import models
from django.utils.text import slugify
from django import template
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50 , verbose_name = 'اسم القسم')

    def __str__(self):
        return self.name

class Book (models.Model):
    name = models.CharField(max_length =50 ,  verbose_name = 'اسم الكتاب')
    category = models.ForeignKey(Category,related_name = "Books_category" ,on_delete=models.CASCADE , verbose_name = 'قسم الكتاب')
    descripton = models.TextField(max_length = 600, verbose_name = 'تفاصيل عن الكتاب')
    img = models.ImageField(upload_to ='Books',default= 'default.png' ,verbose_name = 'صورة الكتاب')
    slid2 =models.ImageField(upload_to ='Books', default= 'default.png',verbose_name = ' الصوره الثانيه')
    slid3 =models.ImageField(upload_to ='Books', default= 'default.png',verbose_name = ' الصوره الثالثه')
    count_of_download=models.IntegerField(blank=True , null = True, verbose_name = 'عدد التحميلاات')

    file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name = 'رفع الملف')
    url = models.CharField(max_length=500, blank=True, null=True)
    created_in = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    
  