from django.db import models

# Create your models here.
class Contact(models.Model):
        
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    msg_type = models.CharField(max_length = 100)
    msg_content = models.TextField(max_length = 300)
