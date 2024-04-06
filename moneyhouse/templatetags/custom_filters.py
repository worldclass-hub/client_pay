from django import template

register = template.Library()

@register.filter
def capitalize_first_letter(value):
    if value:
        return value[0].upper() + value[1:].lower()
    return value
