from api.models import ProductModel
class Cart():
    def __init__(self, request):
        self.session = request.session
        # get current session key
        cart = self.session.get('session_key')
        # if no session key, create new user
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        # Assign cart to self.cart
        self.cart = cart

    def add(self, product):
        product_id = str(product.product_id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_cart_product(self):
        cart_product_ids =list(self.cart.keys())
        print(cart_product_ids)
        products = ProductModel.objects.filter(product_id__in = cart_product_ids)
        return products