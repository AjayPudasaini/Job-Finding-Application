import django_filters
from django_filters import ChoiceFilter
from jobs.models import JobPost
from jobs.models import (JOB_AVALIABLE_TIME)


class FilterTime(django_filters.FilterSet):

    class Meta():
        model = JobPost
        fields = ['AvaliableTime', 'JobCategory', 'JobShift', 'JobLevel', 'Gender']
