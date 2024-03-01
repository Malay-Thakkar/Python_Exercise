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
    path('stock/', views.stock, name="stock"),
    path('crudproduct/', views.crudproduct, name="crudproduct"),
    path('delete/<int:productid>', views.del_product,name="deleteproduct"),
    path('delete_product', views.delete_single_product,name="delete_single_product"),

    path('todolist/', views.apiOverview, name="todolist"),
    path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    
]
