from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('products/',views.list_products,name='products'),
    path('product_details/<id>',views.details_product,name='product_details'),
   
]
