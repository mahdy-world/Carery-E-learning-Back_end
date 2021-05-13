from django.db import models


# Choices 
JOBS = {
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),

}

GENDER = {
    ('ذكر','ذكر'),
    ('انثي','انثي'),
}


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    image = models.ImageField()
    facebook = models.CharField(max_length = 240)
    instagram = models.CharField(max_length = 240)
    twitter = models.CharField(max_length = 240)
    linked_in = models.CharField(max_length = 240)
    gender = models.CharField(max_length=40, choices=GENDER , verbose_name="النوع")
    job = models.CharField(max_length=40, choices=JOBS)
