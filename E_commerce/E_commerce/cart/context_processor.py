from cart.cart import Cart
from cart.wishlist import Wishlist

def cart(request):
    return {'cart':Cart(request)}

def wishlist(request):
    return {'wishlist':Wishlist(request)}