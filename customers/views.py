from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from customers.models import customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    customer_details=None
    error_login_message=None
    if request.POST and 'register' in request.POST:
        context['register']=True   
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        adderss=request.POST.get('address')
        try:  
            user=User.objects.create_user(username=username,password=password,email=email)
            customer_details=customer.objects.create(user=user,phone=phone,address=adderss)
           
        except Exception as e:
            
            error_message="Duplicate username or invalid inputs"
            messages.error(request,error_message)


      #Login django codes      
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password) 
        if user:
            login(request,user) 
            return redirect('home') 
        else:
            error_login_message="invalid credentials" 
            messages.error(request,error_login_message) 
                 
    return render(request,'customer_HTML/account.html',context)