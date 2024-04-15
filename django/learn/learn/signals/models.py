from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ProfileModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    
@receiver(post_save,sender=ProfileModel)
def send_notification(sender, instance, **kwargs):
    print("car object created")
    print(sender,receiver,kwargs)