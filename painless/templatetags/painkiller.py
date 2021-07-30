from django import template 
register = template.Library() 

@register.filter('price_comma_seperator')
def price_comma_seperator(value, arg=''):
    """Seperate comma by each 3 characters"""
    return "{0:,}".format(int(value))