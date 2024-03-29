from django.urls import path
from .views import dashboard,admincategory,adminorder,adminproducts,adminuser,adminproductsdelete,adminproductsupdate

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('order/',adminorder,name="adminorder"),
    path('products/',adminproducts,name="adminproducts"),
    path('productsupdate/<int:product_id>/', adminproductsupdate, name="adminproductsupdate"),
    path('productsdelete/<int:product_id>/', adminproductsdelete, name="adminproductsdelete"),
    path('category/',admincategory,name="admincategory"),
    path('users/',adminuser,name="adminuser"),
]
