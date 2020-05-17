from django import template

register = template.Library()

@register.filter(name='get_related_comments')
def get_related_comments(album):
	return album.comments_set.all()