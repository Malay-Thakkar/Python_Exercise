from django.urls import path
from .views import signin,signup,signout,resetpasswd,home
urlpatterns = [
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="sigout"),
    path('forgatepasswoard/',resetpasswd,name="sigout"),
    path('',home,name="home")
]
