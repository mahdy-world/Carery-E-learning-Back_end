from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

GENDER = {
    ('ذكر','ذكر'),
    ('انثي','انثي'),
}

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile_user", verbose_name = 'المستخدم')
    country = models.ForeignKey(Country, related_name="user_country", on_delete=models.CASCADE , null=True , blank = True , verbose_name = 'البلد')
    gender = models.CharField(max_length=40, choices=GENDER , verbose_name="النوع" )
    phone = models.CharField(max_length=20 , null=True , blank=True)
    image = models.ImageField( upload_to='profile/', verbose_name = 'الصورة الشخصية', null=True , blank = True )

    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)




