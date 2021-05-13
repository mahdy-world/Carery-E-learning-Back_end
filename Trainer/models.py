from django.db import models
GENDER= {
    ('',''),
    ('',''),
}

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    image = models.ImageField()
    facebook = models.CharField(max_length = 240)
    instagram = models.CharField(max_length = 240)
    twitter = models.CharField(max_length = 240)
    linked_in = models.CharField(max_length = 240)
    gender = models.CharField(max_length=40, choices=GENDER)