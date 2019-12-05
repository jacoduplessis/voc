from django.utils.html import mark_safe
from django import template
from django.template.defaultfilters import stringfilter
from markdown import markdown as to_markdown

register = template.Library()


@register.filter
@stringfilter
def markdown(val):
    return mark_safe(to_markdown(val))
