from django.urls import path
from .views import dashboard,admincategory,adminorder,adminproducts,adminuser,adminproductsdelete,adminproductsupdate,adminproductadd,admincategoryadd,admincategorydelete,admincategoryupdate,searchproduct,searchcategory

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('order/',adminorder,name="adminorder"),
    
    path('products/',adminproducts,name="adminproducts"),
    path('searchproduct/',searchproduct, name='searchproduct'),
    path('adminproductadd/',adminproductadd,name="adminproductadd"),
    path('productsupdate/<int:product_id>/', adminproductsupdate, name="adminproductsupdate"),
    path('productsdelete/<int:product_id>/', adminproductsdelete, name="adminproductsdelete"),
    
    path('category/',admincategory,name="admincategory"),
    path('searchcategory/',searchcategory, name='searchcategory'),
    path('categoryadd/',admincategoryadd,name="admincategoryadd"),
    path('categoryupdate/<int:category_id>/', admincategoryupdate, name="admincategoryupdate"),
    path('categorydelete/<int:category_id>/', admincategorydelete, name="admincategorydelete"),
    
    path('users/',adminuser,name="adminuser"),
]
