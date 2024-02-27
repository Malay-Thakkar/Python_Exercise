from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutuser, name="logout"),
    path('about-us/', views.aboutus,name="about"),
    path('contact/', views.contact),
    path('product/', views.product,name="product"),
    path('product/<int:productid>', views.productdetail),
]
