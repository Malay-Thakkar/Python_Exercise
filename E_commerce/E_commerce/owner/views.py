from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.models import ProductModel,CategoryModel
import requests
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.


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

def adminuser(request):
    if request.user.is_staff:
        return render(request,"adminuser.html")
    return redirect('/')    

def admincategory(request):
    if request.user.is_staff:
        categorys = CategoryModel.objects.all()
        return render(request,"admincategory.html",{'Categorys':categorys})
    return redirect('/')

def admincategoryadd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            category = request.POST.get('category')
            if CategoryModel.objects.filter(category=category).exists():
                messages.error(request, f"A {category}' already exists!")
                return redirect('/admin/products/')
            if not category:
                    messages.error(request,"All fields are required!")
            newcategory = CategoryModel(
                category=category
            )    
            newcategory.save()
            messages.success(request,"category added successfully!!!")
            return redirect('/admin/category/')
    return redirect('/')

def admincategoryupdate(request, category_id):
    if request.user.is_staff:
        if request.method == 'POST':
            category_obj = CategoryModel.objects.get(category_id=category_id)
            if category_obj:
                new_category_name = request.POST.get('category')
                if not new_category_name:
                    messages.error(request, "All fields are required!")
                    return redirect('/admin/category/')
                else:
                    category_obj.category = new_category_name
                    category_obj.save()
                    messages.success(request, "Category updated successfully!!!")
                    return redirect('/admin/category/')
            else:
                return render(request, "404.html", {'error': "Category not found"})
    return redirect('/')

def admincategorydelete(request,category_id):
    if request.user.is_staff:
        if request.method == 'POST':
            category = CategoryModel.objects.get(category_id=category_id)
            if category:
                category.delete()
                messages.error(request,"category deleted successfully!!!")
                return redirect('/admin/category/')
            else:
                return render(request,"404.html",{'error':"category not found"})
    return redirect('/')
    
def adminproducts(request):
    if request.user.is_staff:
        domain = request.get_host()
        products = ProductModel.objects.all()
        categorys = CategoryModel.objects.all()
        return render(request,"adminproduts.html",{'products':products,'categorys':categorys,'domain':domain})
    return redirect('/')

def adminproductadd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            unit = request.POST.get('unit')
            stock = request.POST.get('stock')
            img = request.FILES.get('img')
            desc = request.POST.get('desc')
            category_id = request.POST.get('category')
            
            # Move the print statement after the category variable is assigned
            category = get_object_or_404(CategoryModel, pk=category_id)
             
            # Check if a product with the same name already exists
            if ProductModel.objects.filter(name=name).exists():
                messages.error(request, f"A product with the name '{name}' already exists!")
                return redirect('/admin/products/')
            
            if not name or not price or not unit or not stock or not img or not desc or not category:
                messages.error(request, "All fields are required!")
                return redirect('/admin/products/')
            
            newproduct = ProductModel(
                name = name,price = price,unit = unit,stock = stock,img = img,desc = desc,category = category
            )
            newproduct.save()
            messages.success(request,"product added successfully!!!")
            return redirect('/admin/products/')
        return redirect('/')

def adminproductsupdate(request, product_id):
    if request.user.is_staff:
        if request.method == 'POST':
            product = ProductModel.objects.get(product_id=product_id)
            if product:
                name = request.POST.get('name')
                price = request.POST.get('price')
                unit = request.POST.get('unit')
                stock = request.POST.get('stock')
                img = request.FILES.get('img')
                desc = request.POST.get('desc')
                category_id = request.POST.get('category')
                
                # Move the print statement after the category variable is assigned
                category = get_object_or_404(CategoryModel, pk=category_id)

                if not name or not price or not unit or not stock or not img or not desc or not category:
                    messages.error(request, "All fields are required!")
                    return redirect('/admin/products/')
                
                product.name = name
                product.price = price
                product.unit = unit
                product.stock = stock
                product.img = img
                product.desc = desc
                product.category = category
                product.save()
                messages.success(request,"product updated successfully!!!")
                return redirect('/admin/products/')
            else:
                messages.error(request,"product not found")
                return render(request, "404.html", {'error': "Product ID not found"})
    return redirect('/')

    
def adminproductsdelete(request, product_id):
    if request.user.is_staff:
        if request.method == 'POST':
            product = ProductModel.objects.get(product_id=product_id)
            if product:
                product.delete()
                messages.error(request,"product deleted successfully!!!")
                return redirect('/admin/products/')
            else:
                return render(request,"404.html",{'error':"product id not found"})
    return redirect('/')
    
def searchproduct(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            results = ProductModel.objects.filter(Q(name__icontains=query) | Q(category__category__icontains=query))
            context = {'products': results}
            return JsonResponse({'html': render(request, 'search_products.html', context).content.decode('utf-8')})
    return JsonResponse({'html': ''})

def searchcategory(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            results = CategoryModel.objects.filter(Q(category__icontains=query))
            context = {'Categorys': results}
            return JsonResponse({'html': render(request, 'search_category.html', context).content.decode('utf-8')})
    return JsonResponse({'html': ''})