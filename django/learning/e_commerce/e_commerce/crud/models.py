from django.db import models

class signup(models.Model):
    name=models.CharField(max_length=120)
    contact=models.CharField(max_length=12)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    zip=models.CharField(max_length=10)
    tandc=models.CharField(max_length=10)
    date=models.DateField()
    
class contact(models.Model):
    name=models.CharField(max_length=120)
    contact=models.CharField(max_length=12)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    tandc=models.CharField(max_length=10)
    date=models.DateField()
    
class product(models.Model):
    product_name=models.CharField(max_length=120)
    product_id=models.CharField(max_length=120)
    product_dict=models.CharField(max_length=120)
    product_price=models.CharField(max_length=120)
    
class stock(models.Model):
    product_name=models.CharField(max_length=120)
    product_id=models.CharField(max_length=120)
    product_price=models.CharField(max_length=120)
    
class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title