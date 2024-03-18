from django.contrib.auth.models import AbstractUser,User
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12, blank=True)
    Address = models.TextField(blank=True)

    # Add any other custom fields you need

    def __str__(self):
        return self.username