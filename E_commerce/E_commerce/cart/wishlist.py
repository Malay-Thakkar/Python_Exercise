from api.models import ProductModel
from customer.models import CustomUser

class Wishlist():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        wishlist = self.session.get('wishlist')
        if 'wishlist' not in request.session:
            wishlist = self.session['wishlist'] = {}
        self.wishlist = wishlist
    
    def db_add_wishlist(self, product):
        product_id = str(product)
        if product_id in self.wishlist:
            pass
        else:
            self.wishlist[product_id] = {}
        self.session.modified = True
        
        #for login user to store in db 
        if self.request.user.is_authenticated:
            current_user = CustomUser.objects.filter(id = self.request.user.id)
            likeproduct = str(self.wishlist)
            likeproduct = likeproduct.replace("\'","\"")
            current_user.update(old_wishlist=likeproduct) 
              
    def add(self, product):
        product_id = str(product.product_id)
        if product_id in self.wishlist:
            pass
        else:
            self.wishlist[product_id] = {'name': product.name, 'price': product.price}
        self.session.modified = True
        
        #for login user to store in db 
        if self.request.user.is_authenticated:
            current_user = CustomUser.objects.filter(id = self.request.user.id)
            likeproduct = str(self.wishlist)
            likeproduct = likeproduct.replace("\'","\"")
            current_user.update(old_wishlist=likeproduct)

    def __len__(self):
        return len(self.wishlist)
    
    def delete(self, product_id):
        if str(product_id) in self.wishlist:
            del self.wishlist[str(product_id)]
            self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = CustomUser.objects.filter(id = self.request.user.id)
            likeproduct = str(self.wishlist)
            likeproduct = likeproduct.replace("\'","\"")
            current_user.update(old_wishlist=likeproduct)
        
    def get_wishlist_product(self):
        wishlist_product_ids = list(self.wishlist.keys())
        products = ProductModel.objects.filter(product_id__in=wishlist_product_ids)
        return products
    