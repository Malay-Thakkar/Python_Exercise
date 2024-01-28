class Product:
    discount = 0.8
    productlist = []
    def __init__(self, name, price:int, quntity=0):   #constructer: when object creates then execute #here define price must be intiger
        #run validation to recived argument
        #assert use for makeing condition and nevigate msg to user
        assert price >= 0 #not nessessory to write a msg but it convinent to write it 
        assert quntity >= 0,f"{quntity} can not be less then 0"
        
        
        #assign self object and prints
        self.name = name
        self.price = price
        self.quntity = quntity
        print(f"The product name: {name}\n product price: {price}\n product quntity {quntity}")
        
        #add product in priductlist
        Product.productlist.append(self)
        
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quntity}')"
    
    def calculate_total_price(self):
        return self.price * self.quntity
    
    def calculate_total_price(self,price,quntity):
        return price*quntity

    def apply_discount(self):
        self.price = self.price * self.discount # product.discount => best practice is use instace level it can not over write class level  
        print(f"{self.name} price is {self.price}")
        
#Access class attribute 
#print(Product.discount)
#print(Product.__dict__)  # print all atrribute of class and object


#create a object
phone = Product("Phone",1000,5)
laptop = Product("Laptop",10000,3)
tablate = Product("Tablate",5000)      # it will take quntity as predefin
#print(phone.__dict__)#print all phone object attributes
# for instace in Product.productlist:
#    print(instace.name)               #added item in product list
#print(Product.productlist)     #after adding reper method it will display otwer wise it display object id

#create a object with making fail to assert condition
#demo = Product("demophone", 1235,-2)


#using class level attribute apply discount
# phone.apply_discount()
#laptop.discount = 0.7
#laptop.apply_discount()


#print(phone.calculate_total_price(phone.price,phone.quntity))
#print(laptop.calculate_total_price())