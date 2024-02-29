from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from crud.models import signup as SignupModel,contact as ContactModel,product as productModel,stock as stockModel
from datetime import datetime  
from .serializer import ProductSerializer
from rest_framework.renderers import JSONRenderer
from .forms import stockForm,productForm
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
    form = productForm()
    context = {'form': form}  # Initialize context
    
    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            stu = product.objects.all()
            serializer = ProductSerializer(stu, many=True)
            context['data'] = serializer.data  # Add data to context
            context['msg'] = 'Data created successfully'  # Add success message to context
        else:
            context['msg'] = 'Form validation failed'  # Add validation error message to context
    
    return render(request, 'crudproduct.html', context)



def productdetail(request,productid):
    product = productModel.objects.get(product_id = productid)
    serializer = ProductSerializer(product) 
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data,content_type='application/json')


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