from django.urls import path
from .views import dashboard,admincategory,adminorder,adminproducts,adminuser,adminproductsdelete,adminproductsupdate,adminproductadd,admincategoryadd,admincategorydelete,admincategoryupdate,searchproduct,searchcategory,adminorderdetail,adminorderadd,product_add_in_order,adminorderdetailupdate,adminorderdetaildelete,adminuserdetail,adminuserdetailupdate,adminuserdelete

urlpatterns = [
    path('',dashboard,name="dashboard"),
    
    path('order/',adminorder,name="adminorder"),
    path('order/<int:order_id>/',adminorderdetail,name="adminorderdetail"),
    path('orderadd/',adminorderadd,name="adminorderadd"),
    path('orderadd/productadd',product_add_in_order,name="product_add_in_order"),
    path('orderupdate/<int:order_id>/',adminorderdetailupdate,name="adminorderdetailupdate"),
    path('orderdelete/<int:order_id>/',adminorderdetaildelete,name="adminorderdetaildelete"),
    
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
    path('user/<int:user_id>',adminuserdetail,name="adminuserdetail"),
    path('userupdate/<int:user_id>',adminuserdetailupdate,name="adminuserdetailupdate"),
    path('userdelete/<int:user_id>',adminuserdelete,name="adminuserdelete"),
]
