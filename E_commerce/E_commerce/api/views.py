from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib import messages
from api.models import ProductModel,CategoryModel,UploadProduct
from api.serializers import ProductSerializers,CategorySerializers
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
import pandas as pd


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset =ProductModel.objects.all()
    serializer_class = ProductSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset =CategoryModel.objects.all()
    serializer_class = CategorySerializers
    
    @action(detail=True,methods=['get'])
    def product(self,request,pk=None):
        category = CategoryModel.objects.get(pk=pk)
        filter_product=ProductModel.objects.filter(category=category)
        filter_product_serializers=ProductSerializers(filter_product,many=True,context={'request':request})
        return Response(filter_product_serializers.data)
    
    
@login_required(login_url='/signin')
def uploadproductfile(request):
    if request.user.is_staff:
        if request.method == "POST":
            file = request.FILES['files']
            obj = UploadProduct.objects.create(file=file) 
            create_db(obj.file)
            
            return messages.success(request, "File uploaded successfully")
        else:
            return messages.error(request, "Invalid request method")
    else:
        return redirect('/')
    
    
def create_db(file_path):
    df = pd.read_csv(file_path,delimiter=",")
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        ProductModel.objects.create(
            name = l[0],
            price = l[1],
            unit = l[2],
            stock = l[3],
            desc = l[4],
            img = l[5],
            category = CategoryModel.get_list_or_404(l[6])
        )
    print(list_of_csv)