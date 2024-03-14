from django.urls import path
from .views import signup,signin,home,signout,delete_object
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="Home"),
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="sigout"),
    path('media/files/<path:file_path>/',home, name='getfile'),
    path('delete/<int:obj_id>/', delete_object, name='delete_object'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
