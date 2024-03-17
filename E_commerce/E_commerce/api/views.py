from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import ProductModel,CategoryModel
from api.serializers import ProductSerializers,CategorySerializers
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset =ProductModel.objects.all()
    serializer_class = ProductSerializers
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset =CategoryModel.objects.all()
    serializer_class = CategorySerializers
    
    @action(detail=True,methods=['get'])
    def product(self,request,pk=None):
        category = CategoryModel.objects.get(pk=pk)
        filter_product=ProductModel.objects.filter(category=category)
        filter_product_serializers=ProductSerializers(filter_product,many=True,context={'request':request})
        return Response(filter_product_serializers.data)