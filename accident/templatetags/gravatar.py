import hashlib
import urllib
import urllib.parse
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# return only the URL of the gravatar
# default link to default image of avatar
# TEMPLATE USE:
# {% load gravatar %}
# {{ email|gravatar_url:150 }}


@register.filter
def gravatar_url(email, size=40):
    email = email.encode('utf-8')
    default = "http://yogasara.staff.gunadarma.ac.id/photo.jpg"
    gravatar_url = "https://www.gravatar.com/avatar/{}?{}"
    return gravatar_url.format(hashlib.md5(email.lower()).hexdigest(), urllib.parse.urlencode({'d': default, 's': str(size)}))

# return an image tag with the gravatar
# TEMPLATE USE:
# {% load gravatar %}
# {{ email|gravatar:150 }}

@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="{}" height="{}" width="{}">'.format(url, size, size))
