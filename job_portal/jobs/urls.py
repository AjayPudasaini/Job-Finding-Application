from django.urls import path, include
from account import views
from jobs import views as JobsView
from account.views import (  BrowseJobView, JobseekerDashboardView, EmployerProfileView, 
                             JobseekerProfileUpdateView)

from jobs.views import ( JobPostCreateView, my_job_post_view )
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('employer/', include(([
        path('job/post', JobPostCreateView.as_view(), name='job_post'),
        path('my/jobs', my_job_post_view.as_view(), name='my_job_list')

    ], 'jobs.views'), namespace='jobs_employer')),

]
