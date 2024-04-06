from django import template

register=template.Library()

@register.simple_tag(name='getstatus')

def get_status(status):
    status=status-1
    status_arrey=['Confirmed','Processed','Delivered','Rejected']
    return status_arrey[status]

   