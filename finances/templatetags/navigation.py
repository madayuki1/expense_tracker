from django import template

register = template.Library()

def active_nav(request, section):
    