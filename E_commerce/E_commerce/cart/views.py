from django.shortcuts import render, get_object_or_404
from api.models import ProductModel
from django.http import JsonResponse
from .cart import Cart


# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products =cart.get_cart_product
    return render(request,'cart.html',{'cart_products':cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        # product_id = request.POST.get('product_id')
        #get from DB
        product = get_object_or_404(ProductModel,product_id=product_id)
        cart.add(product=product)
        cart_quantity = len(cart)
        # cart_quantity = cart.__len__()
        response =JsonResponse({'cart_quantity':cart_quantity})
        print("\n\n\n\n\n\n",response)
        return response

def cart_delete(request):
    return render(request,'cart.html')

def cart_update(request):
    return render(request,'cart.html')