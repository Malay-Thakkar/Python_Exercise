from django.urls import path
from .views import signin,signup,signout,forgotpasswd,home,tandc,product,productdetail,profile,notfound,aboutus,contactus,thankyou,productfilter,updateuser,changepasswd,deleteuser,search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="sigout"),
    path('terms-and-Conditions/',tandc,name="tandc"),
    path('profile/',profile,name="profile"),
    path('updateuser/',updateuser,name="updateuser"),
    path('changepasswd/',changepasswd,name="changepasswd"),
    path('forgotpasswd/',forgotpasswd,name="forgotpasswd"),
    path('deleteuser/',deleteuser,name="deleteuser"),
    path('',home,name="home"),
    path('product/',product,name="product"),
    path('product/<int:productid>',productdetail,name="productdetail"),
    path('productfilter/<str:categoryid>',productfilter,name="productfilter"),
    path('search/',search,name="search"),
    path('aboutus/',aboutus,name="aboutus"),
    path('contactus/',contactus,name="contactus"),
    path('404/',notfound,name="notfound"),
    path('thankyou/',thankyou,name="thankyou"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)