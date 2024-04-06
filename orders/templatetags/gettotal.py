from django import template

register=template.Library()

@register.simple_tag(name='gettotal')

def get_total(cart):
    total=0
    for items in cart.added_items.all():
        total += items.quantity*items.product.price
        
    return total    

   