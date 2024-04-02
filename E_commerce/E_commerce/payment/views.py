from django.shortcuts import render,redirect,get_object_or_404
from cart.cart import Cart
from payment.models import Order,OrderItems,Payment,ShippingAddressModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/signin')
def checkout(request):
    cart=Cart(request)
    cart_products =cart.get_cart_product()
    cart_quantity =cart.get_quantity()
    total = cart.cart_total()
    gsttotal = cart.cart_gsttotal()
    return render(request,"checkout.html",{'cart_products':cart_products,'cart_quantity':cart_quantity,'total':total,'gsttotal':gsttotal})

@login_required(login_url='/signin')

def place_order(request):
    if request.method == 'POST':
        # Retrieve payment method from the request POST data
        # payment_method = request.POST.get('payment_method')
        payment_method = 'cash'

        # Validate payment method
        if not payment_method:
            messages.error(request, 'Please select a payment method.')
            return redirect('checkout')  # Redirect back to the checkout page

         # Retrieve shipping address data from the form
        shipping_first_name = request.POST.get('shipping_first_name')
        shipping_last_name = request.POST.get('shipping_last_name')
        shipping_phone = request.POST.get('shipping_phone')
        shipping_email = request.POST.get('shipping_email')
        shipping_address = request.POST.get('shipping_address')
        shipping_city = request.POST.get('shipping_city')
        shipping_state = request.POST.get('shipping_state')
        shipping_note = request.POST.get('shipping_note')

        # Retrieve user's cart items
        cart=Cart(request)
        cart_items = request.user.cart_items.all()
        order_total = cart.cart_gsttotal()

        # Create a new Payment instance
        payment = Payment.objects.create(
            user=request.user,
            payment_method=payment_method,
            amount_paid=order_total,
            status='Not_Completed'
        )

        # Create a new ShippingAddressModel instance
        shipping_address = ShippingAddressModel.objects.create(
            user=request.user,
            shipping_first_name=shipping_first_name,
            shipping_last_name=shipping_last_name,
            shipping_phone=shipping_phone,
            shipping_email=shipping_email,
            shipping_address=shipping_address,
            shipping_city=shipping_city,
            shipping_state=shipping_state,
            shipping_note=shipping_note
        )

        # Create a new Order instance
        order = Order.objects.create(
            user=request.user,
            payment=payment,
            full_name=f"{shipping_first_name} {shipping_last_name}",
            order_total=order_total
        )

        # Create OrderItems instances and link them to the order
        for item in cart_items:
            OrderItems.objects.create(
                order=order,
                product=item.product,
                user=request.user,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear the user's cart
        request.user.cart_items.all().delete()

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('/')  # Redirect to a success page
    
    else:
        messages.error(request, 'Please correct the errors in the shipping address form.')
        return redirect('checkout')  # Redirect back to the checkout page with errors
   
