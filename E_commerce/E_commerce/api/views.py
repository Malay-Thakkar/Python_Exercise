from django.shortcuts import render
from rest_framework import viewsets
from api.models import ProductModel,CategoryModel
from api.serializers import ProductSerializers,CategorySerializers
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset =ProductModel.objects.all()
    serializer_class = ProductSerializers
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset =CategoryModel.objects.all()
    serializer_class = CategorySerializers