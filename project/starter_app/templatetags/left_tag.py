from django import template
register = template.Library()
@register.inclusion_tag('starter_app/left_tag.html')
def show_resultsx(mes):
	
    return {'messages': mes}
    