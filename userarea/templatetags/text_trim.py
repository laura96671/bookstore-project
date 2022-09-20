from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def text_trim(value):
    return value[:300] + "..."
