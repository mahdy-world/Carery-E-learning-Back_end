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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , verbose_name = 'المستخدم')
    name = models.CharField( max_length=50 ,verbose_name = 'اسم الطالب' )
    country = models.ForeignKey(Country, related_name="user_country", on_delete=models.CASCADE ,null=True , verbose_name = 'البلد')
    gender = models.CharField(max_length=40, choices=GENDER , verbose_name="النوع")
    phone = models.CharField( max_length=50, null=True , blank=True , verbose_name="رقم الهاتف")
    image = models.ImageField( upload_to='profile/', verbose_name = 'الصورة الشخصية')
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


