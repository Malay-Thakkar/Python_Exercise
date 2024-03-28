from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.models import CustomUser
from api.models import ProductModel,CategoryModel
# Create your views here.

def dashboard(request):
    if request.user.is_staff:
        return render(request,"dashboard.html")
    return redirect('/')


def adminorder(request):
    if request.user.is_staff:
        return render(request,"adminorder.html")
    return redirect('/')

def adminproducts(request):
    if request.user.is_staff:
        domain = request.get_host()
        products = ProductModel.objects.all()
        return render(request,"adminproduts.html",{'products':products,'domain':domain})
    return redirect('/')

def admincategory(request):
    if request.user.is_staff:
        categorys = CategoryModel.objects.all()
        return render(request,"admincategory.html",{'categorys':categorys})
    return redirect('/')

def adminuser(request):
    if request.user.is_staff:
        return render(request,"adminuser.html")
    return redirect('/')