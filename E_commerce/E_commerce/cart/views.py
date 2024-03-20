from django.shortcuts import render, get_object_or_404
from api.models import ProductModel
from django.http import JsonResponse
from .cart import Cart


# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products =cart.get_cart_product
    cart_quantity =cart.get_quantity
    return render(request,'cart.html',{'cart_products':cart_products,'cart_quantity':cart_quantity})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        print(product_id,product_qty)
        #get from DB
        product = get_object_or_404(ProductModel,product_id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity = len(cart)
        # cart_quantity = cart.__len__()
        response =JsonResponse({'cart_quantity':cart_quantity})
        return response

def cart_delete(request):
    return render(request,'cart.html')

def cart_update(request):
    return render(request,'cart.html')