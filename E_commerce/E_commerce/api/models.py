from django.db import models

# Create your models here.
    
#class category
class CategoryModel(models.Model):
    category_id=models.AutoField(primary_key=True)
    category = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.category
    
#model of product
class ProductModel(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    unit=models.CharField(max_length=20)
    stock=models.FloatField()
    disc=models.CharField(max_length=150)
    img=models.FileField()
    category =models.ForeignKey(CategoryModel,on_delete =models.CASCADE)


#class bills