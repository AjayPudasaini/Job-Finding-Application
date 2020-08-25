from django import template

from jobs.models import JobApply

register = template.Library()


@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = JobApply.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False
