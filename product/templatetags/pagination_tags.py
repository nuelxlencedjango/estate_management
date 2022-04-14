from base64 import encode
from django import template
from urllib.parse import urlencode


register = template.Library()

@register.simple_tag
def url_replace (request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value

    return dict_.urlencode()



@register.simple_tag
def my_url(value,field_name,urlencode=None):
    url ='?{}={}'.format(field_name,value)

    if urlencode:
        querystring = urlencode.split('&')
        filteres_querystring = filter(lambda p:p.split('=')[0]!=field_name,querystring)
        encodeed_querystring ='&'.join(filteres_querystring)
        url ='{}&{}'.format(url,encodeed_querystring)

    return url