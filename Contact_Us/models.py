from django.db import models

# Create your models here.
class Contact(models.Model):
        
    name = models.CharField(max_length = 30 , verbose_name = "الاسم")
    email = models.EmailField(verbose_name = "البريد الالكتروني")
    subject = models.CharField(max_length = 100 , verbose_name = "الموضوع")
    message = models.TextField(max_length = 300 , verbose_name = "محتوي الرسالة")

    def __str__(self):
        return self.name