from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from E_commerce.settings import EMAIL_BACKEND, EMAIL_HOST_USER
from customer.models import CustomUser

# Create your views here.
User = get_user_model()
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        Address = request.POST.get('Address')

        if not first_name or not last_name or not username or not email or not password or not phone or not Address:
            messages.error(request, "All fields are required!")
            print(first_name ,last_name,username,email,password,phone,Address)
            return redirect('/signup/')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/signup/')
        user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username,
   			email=email,
            phone=phone,
            Address = Address
		)
        user.set_password(password)
        user.save()
  
        messages.info(request, "Account created Successfully!")
        return redirect('/signin/')
    return render(request, 'signup.html')

def signin(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		if not User.objects.filter(username=username).exists():
			messages.error(request, 'Invalid Username')
			return redirect('/signin/')
		user = authenticate(username=username, password=password)
		
		if user is None:
			messages.error(request, "Invalid Password")
			return redirect('/signin/')
		else:
			login(request, user)
			return redirect('/')
	return render(request, 'signin.html')



def signout(request):
    logout(request)
    return redirect('/signin')

def resetpasswd(request):
    pass

def home(request):
    return render(request,"index.html")

def product(request):
    return render(request,"products.html")

def productdetail(request,productid):
    return render(request,"productdetail.html",{"productid":productid})

def productfilter(request,categoryid):
    return render(request,'productfilter.html',{'categoryid':categoryid})

def tandc(request):
    return render(request,"tandc.html")

def notfound(request):
    return render(request,"404.html")

def thankyou(request):
    return render(request,'thankyou.html')

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        query = request.POST.get('query')
        subject= "Website query"
        message=[name,phone,address,email,query]
        message_string = '\n'.join(message)
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = ["malay.thakkar@drcsystems.com",email] 
        send_mail(subject, message_string, sender_email, recipient_list)
        return render(request,'thankyou.html')
    return render(request,"contactus.html")

@login_required(login_url='/signin')
def profile(request):
    logged_in_user = request.user
    myuser=CustomUser.objects.filter(username=logged_in_user).values()
    context = {
        'myuser': myuser
    }
    return render(request, 'profile.html', context)


