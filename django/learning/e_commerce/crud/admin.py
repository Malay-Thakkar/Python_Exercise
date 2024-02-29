from django.contrib import admin

# Register your models here.
from crud.models import signup,contact,product,stock


admin.site.register(signup)   
admin.site.register(contact)   
admin.site.register(product)
admin.site.register(stock)