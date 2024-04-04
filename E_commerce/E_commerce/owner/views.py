from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.models import ProductModel,CategoryModel
from payment.models import Order,OrderItems,Payment
from payment.models import Order,OrderItems
from django.contrib.auth import get_user_model
import requests
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

CustomUser = get_user_model()

# ================================ dashboard ============================
@login_required(login_url='/signin')
def dashboard(request):
    if request.user.is_staff:
        return render(request,"dashboard.html")
    return redirect('/')


# ================================ order ============================
@login_required
def adminorder(request):
    if request.user.is_staff:
        orders = Order.objects.all()
        products = ProductModel.objects.all()
        return render(request,"adminorder.html",{'orders':orders,'products':products})
    return redirect('/')

@login_required(login_url='/signin')
def adminorderdetail(request,order_id):
    if request.user.is_staff:
        try:
            order = Order.objects.get(id=order_id)
            # payment = Payment.objects.get(id=orderid)
            order_products = OrderItems.objects.filter(Order=order_id)
            if order:
                return render(request,"adminorderdetails.html",{'order':order,'order_products':order_products})
            else:
                return render(request,"404.html",{'error':"order not found"})
        except Order.DoesNotExist:
            return render(request, "404.html", {'error': "Order not found"})
    return redirect('/')

@login_required(login_url='/signin')
def adminorderadd(request,order_id):
    if request.user.is_staff:
        # Extract data from the form
            full_name = request.POST.get('full_name')
            order_total = request.POST.get('order_total')
            order_status = request.POST.get('order_status')
            order_note = request.POST.get('order_note')

            # Validate form data
            if not (full_name and order_total and order_status):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('adminorderadd')

            # Create a new Payment instance
            payment = Payment.objects.create(
                user=request.user,
                payment_method='cash',  # Assuming default payment method is cash
                amount_paid=order_total,
                status='Not_Completed'
            )

            # Create a new Order instance
            order = Order.objects.create(
                user=request.user,
                payment=payment,
                full_name=full_name,
                order_total=order_total,
                order_status=order_status,
                order_note=order_note
            )

            # Add OrderItems
            # Assuming you have a list of items in the request
            items = request.POST.getlist('items')  # Assuming 'items' is a list of dictionaries containing product_id, quantity, etc.

            for item in items:
                product_id = item.get('product_id')
                quantity = item.get('quantity')
                # Get the product based on the ID
                product = ProductModel.objects.get(id=product_id)
                # Create OrderItems instance
                OrderItems.objects.create(
                    order=order,
                    product=product,
                    user=request.user,
                    quantity=quantity,
                    price=product.price,
                    total_price=product.price * quantity
                )

            messages.success(request, 'Order has been added successfully!')
            return redirect('adminorderadd')
            
    return redirect('/')

@login_required(login_url='/signin')
def adminorderdetailupdate(request, order_id):
    if request.user.is_staff:
        pass
    return redirect('/')

@login_required(login_url='/signin')
def adminorderdetaildelete(request, order_id):
    if request.user.is_staff:
        if request.method == 'POST':
            order = Order.objects.get(id=order_id)
            order.delete()
            return redirect('/admin/order')
    return redirect('/')


# ================================ user ============================

@login_required(login_url='/signin')
def adminuser(request):
    if request.user.is_staff:
        users = CustomUser.objects.all()
        return render(request,"adminuser.html",{'users':users})
    return redirect('/')    

@login_required(login_url='/signin')
def adminuserdetail(request, user_id):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=user_id)
        return render(request,"adminuserdetails.html",{'user':user})
    return redirect('/')

@login_required(login_url='/signin')
def adminuseradd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            Address = request.POST.get('Address')
            tandc = request.POST.get('tandc')

            if not first_name or not last_name or not username or not email or not password or not phone or not Address:
                messages.error(request, "All fields are required!")
                return redirect('/signup/')
            
            user = CustomUser.objects.filter(username=username)
            if user.exists():
                messages.info(request, "Username already taken!")
                return redirect('/signup/')
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone=phone,
                Address = Address,
                tandc = tandc
            )
            user.set_password(password)
            user.save()
    
            messages.info(request, "Account created Successfully!")
            return redirect('/admin/users/')
            
    return redirect('/')

@login_required(login_url='/signin')
def adminuserdetailupdate(request, user_id):
    if request.user.is_staff:
        myuser = CustomUser.objects.get(id=user_id)
        context = {
        'myuser': myuser
        }
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            Address = request.POST.get('Address')

            if not first_name or not last_name or not username or not email or not phone or not Address:
                messages.error(request, "All fields are required!")
                return redirect('/admin/users/')
            if username != myuser.username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
                return redirect('/updateuser/')
            
            # Update user object with new values
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.username = username
            myuser.email = email
            myuser.phone = phone
            myuser.Address = Address
            
            myuser.save()

            messages.info(request, "Profile Updated Successfully!")
            return redirect('/admin/users/')
        return render(request, 'updateuser.html', context)
    return redirect('/')

@login_required(login_url='/signin')
def adminuserdelete(request, user_id):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=user_id)
        if request.method == 'POST':
            user.delete()
            messages.error(request,"{user_id}-account is successfully deleted !!!")
            return render(request,"adminuserdetails.html",{'user':user})
        else:
            return render(request,"adminuserdetails.html",{'user':user})
    return redirect('/')



# ================================ category ============================
@login_required(login_url='/signin')
def admincategory(request):
    if request.user.is_staff:
        categorys = CategoryModel.objects.all()
        return render(request,"admincategory.html",{'Categorys':categorys})
    return redirect('/')

@login_required(login_url='/signin')
def admincategoryadd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            category = request.POST.get('category')
            if CategoryModel.objects.filter(category=category).exists():
                messages.error(request, f"A {category}' already exists!")
                return redirect('/admin/products/')
            if not category:
                    messages.error(request,"All fields are required!")
            newcategory = CategoryModel(
                category=category
            )    
            newcategory.save()
            messages.success(request,"category added successfully!!!")
            return redirect('/admin/category/')
    return redirect('/')

@login_required(login_url='/signin')
def admincategoryupdate(request, category_id):
    if request.user.is_staff:
        if request.method == 'POST':
            category_obj = CategoryModel.objects.get(category_id=category_id)
            if category_obj:
                new_category_name = request.POST.get('category')
                if not new_category_name:
                    messages.error(request, "All fields are required!")
                    return redirect('/admin/category/')
                else:
                    category_obj.category = new_category_name
                    category_obj.save()
                    messages.success(request, "Category updated successfully!!!")
                    return redirect('/admin/category/')
            else:
                return render(request, "404.html", {'error': "Category not found"})
    return redirect('/')

@login_required(login_url='/signin')
def admincategorydelete(request,category_id):
    if request.user.is_staff:
        if request.method == 'POST':
            category = CategoryModel.objects.get(category_id=category_id)
            if category:
                category.delete()
                messages.error(request,"category deleted successfully!!!")
                return redirect('/admin/category/')
            else:
                return render(request,"404.html",{'error':"category not found"})
    return redirect('/')
 

# ================================ product ============================
@login_required(login_url='/signin')   
def adminproducts(request):
    if request.user.is_staff:
        domain = request.get_host()
        products = ProductModel.objects.all()
        categorys = CategoryModel.objects.all()
        return render(request,"adminproduts.html",{'products':products,'categorys':categorys,'domain':domain})
    return redirect('/')

@login_required(login_url='/signin')
def adminproductadd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            unit = request.POST.get('unit')
            stock = request.POST.get('stock')
            img = request.FILES.get('img')
            desc = request.POST.get('desc')
            category_id = request.POST.get('category')
            
            # Move the print statement after the category variable is assigned
            category = get_object_or_404(CategoryModel, pk=category_id)
             
            # Check if a product with the same name already exists
            if ProductModel.objects.filter(name=name).exists():
                messages.error(request, f"A product with the name '{name}' already exists!")
                return redirect('/admin/products/')
            
            if not name or not price or not unit or not stock or not img or not desc or not category:
                messages.error(request, "All fields are required!")
                return redirect('/admin/products/')
            
            newproduct = ProductModel(
                name = name,price = price,unit = unit,stock = stock,img = img,desc = desc,category = category
            )
            newproduct.save()
            messages.success(request,"product added successfully!!!")
            return redirect('/admin/products/')
        return redirect('/')

@login_required(login_url='/signin')
def adminproductsupdate(request, product_id):
    if request.user.is_staff:
        if request.method == 'POST':
            product = ProductModel.objects.get(product_id=product_id)
            if product:
                name = request.POST.get('name')
                price = request.POST.get('price')
                unit = request.POST.get('unit')
                stock = request.POST.get('stock')
                img = request.FILES.get('img')
                desc = request.POST.get('desc')
                category_id = request.POST.get('category')
                
                # Move the print statement after the category variable is assigned
                category = get_object_or_404(CategoryModel, pk=category_id)

                if not name or not price or not unit or not stock or not img or not desc or not category:
                    messages.error(request, "All fields are required!")
                    return redirect('/admin/products/')
                
                product.name = name
                product.price = price
                product.unit = unit
                product.stock = stock
                product.img = img
                product.desc = desc
                product.category = category
                product.save()
                messages.success(request,"product updated successfully!!!")
                return redirect('/admin/products/')
            else:
                messages.error(request,"product not found")
                return render(request, "404.html", {'error': "Product ID not found"})
    return redirect('/')

@login_required(login_url='/signin')
def adminproductsdelete(request, product_id):
    if request.user.is_staff:
        if request.method == 'POST':
            product = ProductModel.objects.get(product_id=product_id)
            if product:
                product.delete()
                messages.error(request,"product deleted successfully!!!")
                return redirect('/admin/products/')
            else:
                return render(request,"404.html",{'error':"product id not found"})
    return redirect('/')

@login_required(login_url='/signin')  
def searchproduct(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            results = ProductModel.objects.filter(Q(name__icontains=query) | Q(category__category__icontains=query))
            context = {'products': results}
            return JsonResponse({'html': render(request, 'search_products.html', context).content.decode('utf-8')})
    return JsonResponse({'html': ''})

@login_required(login_url='/signin')
def searchcategory(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            results = CategoryModel.objects.filter(Q(category__icontains=query))
            context = {'Categorys': results}
            return JsonResponse({'html': render(request, 'search_category.html', context).content.decode('utf-8')})
    return JsonResponse({'html': ''})