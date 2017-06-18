import time
import re
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()
MONTH = ('Січень','Лютий','Березень','Квітень','Травень','Червень',
         'Липень','Серпень','Вересень','Жовтень','Листопад','Грудень')
@register.filter
def dateFormating(value):
    res = MONTH[int(value)-1]
    return res
    # form = getattr(settings, format_string)
    # t = time.localtime(float(value))
    # return time.strftime(form,t)


@register.simple_tag(takes_context=True)
def active_url(context, url):
    try:
        pattern = '^%s$' % reverse(url)
    except NoReverseMatch:
        pattern = url
    path = context['request'].path
    return "class=active" if re.search(pattern, path) else ''