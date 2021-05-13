from django.db import models

# Create your models here.

class Book (models.Model):
    name = models.CharField(max_length =50)
    descripton = models.TextField(max_length = 300)
    auther = models.CharField(max_length = 30)