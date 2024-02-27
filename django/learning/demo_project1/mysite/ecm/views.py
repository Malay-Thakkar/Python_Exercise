from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from ecm.models import signup as SignupModel,contact as ContactModel
from datetime import datetime  

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
    if request.user.is_authenticated:
        return redirect("/about-us")
    else:
        return render(request, 'index.html')

def logoutuser(request):
    logout(request)
    return redirect("/signin")


def product(request):
    return HttpResponse('<h1>Product</h1>')

def productdetail(request,productid):
    return HttpResponse(f'your product id :{productid}')


    
