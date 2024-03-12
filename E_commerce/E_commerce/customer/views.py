from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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