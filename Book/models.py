from django.db import models
from django.utils.text import slugify
# Create your models here.

class Book (models.Model):
    name = models.CharField(max_length =50)
    descripton = models.TextField(max_length = 600)
    img = models.ImageField(upload_to ='Books')
    count_of_page = models.IntegerField(blank=True , null = True)
    count_of_download=models.IntegerField(blank=True , null = True)

    file = models.FileField(upload_to='files/%Y/%m/%d')

    def __str__(self):
        return self.name

   