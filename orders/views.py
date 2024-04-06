from django.shortcuts import render,redirect
from . models import order,orderedItem
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,create=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'order_HTML/cart.html',context)


def view_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=order.objects.filter(owner=customer).exclude(order_status=order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'order_HTML/orders.html',context)


def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
        

            order_obj=order.objects.get(
                owner=customer,
                order_status=order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=order.OREDR_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message='Your order is processed. Your item will be delivered within 2 days.'
                messages.success(request,status_message)
            else:
                status_error_message='Unable to proceed.No items in the cart'
                messages.error(request,status_error_message)
        except Exception as e:
            status_error_message='Unable to proceed.'
            messages.error(request,status_error_message)
    return redirect('cart')
            
            

@login_required(login_url='login')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')

        cart_obj,create=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        products=product.objects.get(id=product_id)

        orderd_item,created=orderedItem.objects.get_or_create(
            product=products,
            owner=cart_obj
        )
        if created:
            orderd_item.quantity=quantity
            orderd_item.save()
        else:
              orderd_item.quantity=orderd_item.quantity +quantity
              orderd_item.save()

    return redirect('cart')


def remove_item_from_cart(request,id):
    item=orderedItem.objects.get(id=id)
    if item:
        item.delete()
        return redirect('cart')