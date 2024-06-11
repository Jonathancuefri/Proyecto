from django import template

register = template.Library()

@register.filter
def get_item(obj, key):
    if isinstance(obj, dict):
        return obj.get(key, '')
    elif hasattr(obj, '_meta') and key in [field.name for field in obj._meta.fields]:
        return getattr(obj, key, '')
    else:
        return ''