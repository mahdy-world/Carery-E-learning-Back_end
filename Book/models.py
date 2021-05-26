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
    img = models.ImageField(upload_to ='Books', verbose_name = 'صورة الكتاب')
    count_of_page = models.IntegerField(blank=True , null = True, verbose_name = 'عدد الصفحات')
    count_of_download=models.IntegerField(blank=True , null = True, verbose_name = 'عدد التحميلاات')

    file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name = 'رفع الملف')

    def __str__(self):
        return self.name

    def increment_numdownload(self):
        self.count_of_download +=1
        return self.count_of_download