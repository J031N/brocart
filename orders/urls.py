from django.urls import path
from orders import views


urlpatterns=[
    path('cart/',views.show_cart, name='cart'),
    path('orders/',views.view_orders, name='orders'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('remove_items/<id>',views.remove_item_from_cart,name='remove_items'),
    path('checkout/',views.checkout_cart,name='checkout')
]