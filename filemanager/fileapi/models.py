from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class signup(models.Model):
    name=models.CharField(max_length=120)
    username=models.CharField(max_length=120,default="default_username")
    email=models.EmailField(max_length=120)
    password = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)    

ext = FileExtensionValidator(['pdf','mp4',])

class filesModel(models.Model):
    files = models.FileField(upload_to="files/",validators=[ext])
    fileOwner=models.ForeignKey(User,on_delete=models.CASCADE)