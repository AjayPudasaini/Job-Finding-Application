from django.urls import path, include
from account import views
from jobs import views as JobsView
from account.views import (JobseekerDashboardView, 
                             JobseekerProfileUpdateView)

from jobs.views import ( JobPostCreateView, MyJobDetailView, JobLists )
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('myhomes', JobLists.as_view(), name='homes'),
    path('browse/jobs', JobsView.BrowseJobView, name = 'browse_job'),
    path('job/detail/<int:id>', JobsView.BrowseJobDetail, name='jobs_detail'),

    path('employer/', include(([
        path('job/post', JobPostCreateView.as_view(), name='job_post'),
        # path('my/jobs/<str:username>', MyJobListView.as_view(), name='my_job_list'),
        path('my/jobs/public/preview/<str:username>/<int:pk>', MyJobDetailView.as_view(), name='my_job_detail'),


    ], 'jobs.views'), namespace='jobs_employer')),

    

]
