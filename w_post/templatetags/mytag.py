from markdown import markdown
from django import template

register = template.Library()
@register.filter(name='my_markdown')
def my_markdown(value):
    return markdown(value)
