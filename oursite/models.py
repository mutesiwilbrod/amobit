from django.db import models
from django.utils import timezone

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=30)
    user_password= models.CharField(max_length=8)
    user_email= models.TextField()
    user_phone_number=models.CharField(max_length=10)
