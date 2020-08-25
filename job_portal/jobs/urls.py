from django.urls import path, include
from account import views
from jobs import views as JobsView
from account.views import (JobseekerDashboardView, 
                             JobseekerProfileUpdateView)

from jobs.views import ( JobPostCreateView, MyJobDetailView, JobLists,
                         MyJobUpdateView, MyJobDeleteView, JobApplyCreateView,
                         AppliedJobListView, JobAppliedPerson )
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', JobLists.as_view(), name='homes'),
    path('browse/jobs', JobsView.BrowseJobView, name = 'browse_job'),
    path('job/detail/<int:id>', JobsView.BrowseJobDetail, name='jobs_detail'),
    path('job/save/<int:id>', JobsView.SaveJobs, name='save_jobs'),
    path('saved/jobs', JobsView.ViewSavedJobs, name='saved_jobs'),
    path('job/detail/<int:pk>/apply', JobApplyCreateView.as_view(), name='job_apply'),
    path('applied/jobs/<str:username>', AppliedJobListView.as_view(), name='applied_jobs'),

    path('employer/', include(([
        path('job/post', JobPostCreateView.as_view(), name='job_post'),
        # path('my/jobs/<str:username>', MyJobListView.as_view(), name='my_job_list'),
        path('my/jobs/<int:pk>/update', MyJobUpdateView.as_view(), name='my_job_update'),
        path('my/jobs/<int:pk>/delete', MyJobDeleteView.as_view(), name='my_job_delete'),
        path('my/jobs/public/preview/<str:username>/<int:pk>', MyJobDetailView.as_view(), name='my_job_detail'),
        path('my/jobs/<int:id>/who/applied', JobAppliedPerson.as_view(), name='who_applied_job'),
        path('jobseeker/profile', JobsView.JobseekerProfileView, name='jobseeker_profile')


    ], 'jobs.views'), namespace='jobs_employer')),

    

]
