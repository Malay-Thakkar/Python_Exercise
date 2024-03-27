from django.urls import path
from .views import dashboard,admincategory,adminorder,adminproducts,adminuser

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('order/',adminorder,name="adminorder"),
    path('products/',adminproducts,name="adminproducts"),
    path('category/',admincategory,name="admincategory"),
    path('users/',adminuser,name="adminuser"),
]
