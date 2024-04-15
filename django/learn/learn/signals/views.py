from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def signup(request):
    profileform = ProfileForm(request.POST, request.FILES)
    profilemodelform = ProfileModelForm(request.POST, request.FILES)

    if request.method == "POST":
        ProfileModel.objects.create(
            name="faa", address="safas", phone="546515", email="asd@gmail.com"
        )
        return HttpResponse(request, "success_url")
        # if profilemodelform.is_valid():
        #     profilemodelform.save()
        #     return HttpResponse(request, "success_url")

    return render(
        request,
        "my_template.html",
        {"profileform": profileform, "profilemodelform": profilemodelform},
    )
