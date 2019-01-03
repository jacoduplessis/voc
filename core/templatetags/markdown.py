from django.utils.html import mark_safe
from markdown import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def markdown(val):
    return mark_safe(markdown(val))
