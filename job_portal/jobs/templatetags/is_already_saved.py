from django import template

from jobs.models import JobPost

register = template.Library()


@register.simple_tag(name='is_already_Saved')
def is_already_saved(user):
    saved = JobPost.objects.filter(user=user)
    if saved:
        return True
    else:
        return False
