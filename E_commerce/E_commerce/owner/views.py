from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.models import CustomUser
from api.models import ProductModel,CategoryModel
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def dashboard(request):
    if request.user.is_staff:
        return render(request,"dashboard.html")
    return redirect('/')


@login_required
def adminorder(request):
    if request.user.is_staff:

        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            unit = request.POST.get('unit')
            stock = request.POST.get('stock')
            img = request.FILES.get('image')
            desc = request.POST.get('desc')
            # Now, you can make a POST request to your API to add the product
            print(name,price,stock,img,desc)
            response = requests.post('http://127.0.0.1:8000/api/product/', 
                                    headers={'Authorization': 'Bearer vD7CE0tnwwgqLcNsRKCDNCVk2UjbJXxN'},
                                    data={'name': name, 'price': price, 'stock': stock,'desc':desc,'unit':unit,'img': img})
            print(name,price,stock,img,desc)
            
            # Check if the request was successful
            if response.status_code == 201:  # Assuming the API returns 201 for successful creation
                # Redirect to a success page or any other page
                return redirect('success_page')
            else:
                # Handle error
                return render(request, '404.html', {'error': response.text})

        else:  # GET request
            # Make a GET request to fetch the list of products
            response = requests.get('http://127.0.0.1:8000/api/product/', headers={'Authorization': 'Bearer vD7CE0tnwwgqLcNsRKCDNCVk2UjbJXxN'})
            
            # Check if the API call was successful
            if response.status_code == 200:
                products = response.json()
                return render(request, 'adminorder.html', {'products': products})
            else:
                # Handle error
                return render(request, '404.html', {'error': response.text})
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

def adminproductsupdate(request,product_id):
    if request.user.is_staff:
        prod = ProductModel.objects.get(product_id=product_id)
        if request.method == 'POST':
                product = ProductModel.objects.get(product_id=product_id)
                if product:
                    name = request.POST.get('name')
                    price = request.POST.get('price')
                    unit = request.POST.get('unit')
                    stock = request.POST.get('stock')
                    img = request.FILES.get('image')
                    desc = request.POST.get('desc')
                    category = request.POST.get('category')
                    
                    if not name or not price or not unit or not stock or not img or not desc or not category:
                        messages.error(request, "All fields are required!")
                        return redirect('/admin/products/')
                
                    product.name =name
                    product.price =price
                    product.unit =unit
                    product.stock =stock
                    product.img =img
                    product.desc =desc
                    product.category =category
                    product.save()
                    
                    return redirect('/admin/products/')
                else:
                    return render(request,"404.html",{'error':"product id not found"})
        else: 
            return render(request,"updateproduct.html",{'prod':prod})
    return redirect('/')
    
def adminproductsdelete(request, product_id):
    if request.user.is_staff:
        if request.method == 'POST':
            product = ProductModel.objects.get(product_id=product_id)
            if product:
                product.delete()
                return redirect('/admin/products/')
            else:
                return render(request,"404.html",{'error':"product id not found"})
    return redirect('/')
    