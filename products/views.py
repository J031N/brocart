from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_products=product.objects.order_by('priority')[:4]
    latest_products=product.objects.order_by('-id')[:4]
    context={'featured_products':featured_products,
             'latest_products':latest_products
             }
        
    return render(request,'index.html',context)


def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('pages',1)

    product_list=product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_paginator_list=product_paginator.get_page(page)
    product_dict={'products':product_paginator_list}
    return render(request,'product_HTMl/products.html',product_dict)

def details_product(request,id):
    product_details=product.objects.get(id=id)

    return render(request,'product_HTML/product_details.html',{'product_details_dict':product_details})