from django.urls import path
from .views import signin,signup,signout,resetpasswd,home,tandc,product,productdetail,profile,notfound,aboutus,contactus
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="sigout"),
    path('forgatepasswoard/',resetpasswd,name="sigout"),
    path('',home,name="home"),
    path('terms-and-Conditions/',tandc,name="tandc"),
    path('product/',product,name="product"),
    path('product/<int:productid>',productdetail,name="productdetail"),
    path('profile/',profile,name="profile"),
    path('aboutus/',aboutus,name="profile"),
    path('contactus/',contactus,name="profile"),
    path('404/',notfound,name="notfound"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)