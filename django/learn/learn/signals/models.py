from django.db import models

# Create your models here.


class ProfileModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')