from django.shortcuts import render, get_object_or_404
from api.models import ProductModel
from django.http import JsonResponse
from .cart import Cart
from django.contrib import messages

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products =cart.get_cart_product
    cart_quantity =cart.get_quantity
    total = cart.cart_total()
    return render(request,'cart.html',{'cart_products':cart_products,'cart_quantity':cart_quantity,'total':total})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #get from DB
        product = get_object_or_404(ProductModel,product_id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity = len(cart)
        # cart_quantity = cart.__len__()
        response =JsonResponse({'cart_quantity':cart_quantity})
        messages.success(request,'successfully added Items')
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product_id':product_id})
        messages.success(request,'successfully deleted Items')
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response