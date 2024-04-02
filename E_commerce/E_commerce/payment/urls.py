from django.urls import path
from .views import *

urlpatterns = [
    path('cart/checkout/',checkout,name="checkout"),
    path('cart/checkout/placeorder',place_order,name="placeorder"),
]
