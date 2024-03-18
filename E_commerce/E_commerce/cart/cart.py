class Cart():
    def __init__(self,request):
        self.session = request.session
        #get current session key
        cart = self.session.get('session_key')
        #if no session key create new new user
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}
            
            self.cart = cart