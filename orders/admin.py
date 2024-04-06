from django.contrib import admin
from .models import order,orderedItem


# Register your models here.
class order_admin(admin.ModelAdmin):
    list_filter=[
        'order_status',
        'owner'
    
    ]
    search_fields=(
        'owner__name',
        'id'
    )


admin.site.register(order,order_admin)
admin.site.register(orderedItem)
