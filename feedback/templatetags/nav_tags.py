from django.template import Library
from django.core.urlresolvers import reverse

register = Library()

## tags.py
@register.simple_tag
def active(request, urls):
    try:
        if request.path in ( reverse(url) for url in urls.split() ):
            return "active"
        return ''
    except:
        import re
        if re.match(urls, request.path):
            return 'active'
        return ''

