from django import template

register = template.Library()

@register.simple_tag()
def active_nav(request, section):
    url_name = request.resolver_match.url_name
    if section in url_name:
        return 'active'
