from django import template

register = template.Library()

@register.filter
def filter_canceled(value):
    if value:
        return "ОТМЕНЕН"
    else:
        return ""
