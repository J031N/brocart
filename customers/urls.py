from django.urls import path
from customers import views

urlpatterns = [
    path('login/',views.show_account,name='login'),
    path('logout/',views.sign_out,name='logout')
]
