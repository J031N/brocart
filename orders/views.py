from django.shortcuts import render

# Create your views here.
def show_cart(request):
    return render(request,'order_HTML/cart.html')