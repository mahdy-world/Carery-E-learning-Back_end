from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=30, verbose_name="الاسم")
    job = models.CharField( max_length=50 , null=True , verbose_name="الوظيفة")
    image = models.ImageField(upload_to='traniers/',  verbose_name="الصورة")
    facebook = models.CharField(max_length = 240 , verbose_name="عنوان الفيس بوك")
    instagram = models.CharField(max_length = 240 , verbose_name="عنوان الانستجرام")
    twitter = models.CharField(max_length = 240 , verbose_name="عنوان التويتر")
    linked_in = models.CharField(max_length = 240 , verbose_name="عنوان لينكدان")
    
    def __str__(self):
        return self.name