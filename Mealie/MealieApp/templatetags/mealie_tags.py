from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)

@register.filter
def get_dict_key(dict, key):
    return dict[key]