from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from crud.models import signup as SignupModel,contact as ContactModel,product as productModel,stock as stockModel, Task
from datetime import datetime  
from .serializer import ProductSerializer,TaskSerializer
from crud.forms import stockForm,ProductForm
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')  
        tandc = request.POST.get('tandc')

        # Use SignupModel instead of signup for the model class
        signup_entry = SignupModel(name=name, contact=contact, address=address, email=email,city=city, state=state, zip=zip_code, tandc=tandc,date=datetime.now())
        signup_entry.save()

    return render(request, 'signup.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        tandc = request.POST.get('cmo')

        # Use SignupModel instead of signup for the model class
        contact_entry = ContactModel(name=name, contact=contact, address=address, email=email,tandc=tandc,date=datetime.now())
        contact_entry.save()
        
    return render(request,'contact.html')

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            return redirect("/about-us")
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

from django.contrib.auth.decorators import login_required

@login_required
def aboutus(request):
    dict = {
        "name": "Malay Thakkar",
        "mailid": "its.malaythakkar@gmail.com"
    }
    return render(request, "about.html", dict)

def index(request):
    return render(request,"index.html")

def logoutuser(request):
    logout(request)
    return redirect("/signin")


def product(request):
    product = productModel.objects.all()
    serializer = ProductSerializer(product, many=True)
    context_data = {
        'products': serializer.data
    }
    return render(request,'product.html',context_data)


def crudproduct(request):
    print("called")
    if request.method == "POST":
        print("called")
        fm = ProductForm(request.POST)
        if fm.is_valid():
            print("called")
            fm.save()
            fm = ProductForm()
    else:
        fm =ProductForm()
    products = productModel.objects.all()
    return render(request, 'crudproduct.html', {'form':fm,'products':products})


def delete_single_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        print(product_id)
        try:
            product = productModel.objects.get(product_id=product_id)
        except productModel.DoesNotExist:
            return HttpResponse("Product not found", status=404)
        product.delete()
        return redirect('/crudproduct')

    else:
        return HttpResponse("Method not allowed", status=405)
    
def del_product(request, productid):
    if request.method == 'POST':
        try:
            # Filter all products with the specified product_id and delete them
            products_to_delete = productModel.objects.filter(product_id=productid)
            print("Deleting products:", products_to_delete)
            products_to_delete.delete()
            print("Products deleted successfully.")
            return redirect('/crudproduct')
        except Exception as e:
            return HttpResponse("Error deleting products: " + str(e))
    else:
        return HttpResponse("Invalid request method.")

    
def productdetail(request,productid):
    product = productModel.objects.get(product_id = productid)
    serializer = ProductSerializer(product) 
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data,content_type='application/json')

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

# def product(request):
#     if request.method =="POST":
#         product_name = request.POST.get(product_name)
#         product_price = request.POST.get(product_price)
#         product_dict = request.POST.get(product_dict)
#         product_img = request.POST.get(product_img)
    
#         product_entry =productModel(product_name=product_name,product_price=product_price,product_img=product_img)
#     return HttpResponse('<h1>Product</h1>')


    
def stock(request):
    if request.method=='POST':
        form = stockForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_id = form.cleaned_data['product_id']
            product_price = form.cleaned_data['product_price']

            new_stock = stockModel(product_name=product_name, product_id=product_id, product_price=product_price)
            new_stock.save()
            
            return HttpResponse('success')
    else:
        form = stockForm()
    return render(request, 'stock.html', {'form': form})