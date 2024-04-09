from django.urls import path,include
from api.views import ProductViewSet,CategoryViewSet, uploadproductfile
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'category',CategoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('uploadproduct',uploadproductfile,name="uploadproductfile")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)