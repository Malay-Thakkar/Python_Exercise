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

    def add(self, product,quantity):
        product_id = str(product.product_id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True 

    def __len__(self):
        return len(self.cart)
    
    def get_cart_product(self):
        cart_product_ids =list(self.cart.keys())
        products = ProductModel.objects.filter(product_id__in = cart_product_ids)
        return products
    
    def get_quantity(self):
        quantity=self.cart
        return quantity
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True 
        things = self.cart
        return things
    
    def delete(self,product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
    def cart_total(self):
        quantity = self.cart
        total = 0
        for key, value in quantity.items():
            key = int(key)
            prod = ProductModel.objects.filter(product_id = key).values().first()
            total += (prod['price'] * value)
        return total
        
      
