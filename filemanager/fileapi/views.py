from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import signup,filesModel
from fileapi.forms import FileForm
from django.core.files.storage import default_storage
from django.conf import settings

@login_required(login_url="/signin")
def home(request):
    all_files = filesModel.objects.all()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('files')
            for file in files:
                if not file.name.endswith(('.pdf', '.doc', '.docx', '.mp4')):
                    messages.error(request,f'Unsupported file format: {file.name}. Allowed formats: PDF, DOC, DOCX')
                    return render(request, 'index.html', {'form': form,User:User,'files': all_files })
    
                if file.size > 20000000 :
                    messages.error(request, 'File size must be less than 20MB.')
                    return render(request, 'index.html', {'form': form,User:User,'files': all_files })
                
                filesModel.objects.create(files=file, fileOwner=request.user)
            messages.success(request,"All files uploaded successfully!")
            
        return render(request, 'index.html', {'form': form,User:User,'files': all_files })
    else:
        form = FileForm()
        
    return render(request, 'index.html', {'form': form,User:User,'files': all_files })

@login_required(login_url="/signin")
def delete_object(request, obj_id):  
    try:
        obj = filesModel.objects.get(pk=obj_id)
        temp=str(request.user.username)
        temp1=str(obj.fileOwner)
        if temp == temp1:
            media_path = obj.files.path
            obj.delete()
            if default_storage.exists(media_path):
                default_storage.delete(media_path)
                messages.success(request,"file deleted successfully!")
                return redirect('/')
        else:
            messages.error(request,"You don't have writs to delete a file!")
        return redirect('/')
    except filesModel.DoesNotExist:
        return HttpResponse("not exists")
    
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

def signup(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.filter(username=username)
  
		if user.exists():
			messages.info(request, "Username already taken!")
			return redirect('/signup/')

		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username,
   			email=email
		)
		user.set_password(password)
		user.save()
  
		messages.info(request, "Account created Successfully!")
		return redirect('/signin/')
	return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/signin')
