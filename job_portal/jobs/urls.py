from django.urls import path, include
from account import views
from jobs import views as JobsView
from account.views import (JobseekerProfileUpdateView)

from jobs.views import ( JobPostCreateView, MyJobDetailView, JobLists,
                         MyJobUpdateView, MyJobDeleteView, JobApplyCreateView,
                         AppliedJobListView, JobseekerProfileListView,
                         HowItWorks, JobseekerProfileDetailView,
                         EmployerProfileListView, EmployerProfileDetailView,
                         AboutSmartKTM, )
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', JobLists.as_view(), name='homes'),
    path('browse/jobs', JobsView.BrowseJobView, name = 'browse_job'),
    path('job/detail/<int:id>', JobsView.BrowseJobDetail, name='jobs_detail'),
    path('job/save/<int:id>', JobsView.SaveJobs, name='save_jobs'),
    path('saved/jobs', JobsView.ViewSavedJobs, name='saved_jobs'),
    path('job/detail/<int:pk>/apply', JobApplyCreateView.as_view(), name='job_apply'),
    path('applied/jobs/<str:username>', AppliedJobListView.as_view(), name='applied_jobs'),
    path('how/it/works', HowItWorks.as_view(), name='how_works'),
    path('about/smart/ktm/jobs', AboutSmartKTM.as_view(), name='about_us'),
    path('jobseeker/details/<str:username>/<int:pk>', JobseekerProfileDetailView.as_view(), name='jobseeker_detaillls'),
    path('jobseeker/profile/list', JobseekerProfileListView.as_view(), name='jobseeker_profile'),
    path('employer/details/<str:username>/<int:pk>', EmployerProfileDetailView.as_view(), name='employer_detaillls'),
    path('employer/profile/list', EmployerProfileListView.as_view(), name='employer_profile'),



    path('employer/', include(([
        path('job/post', JobPostCreateView.as_view(), name='job_post'),
        # path('my/jobs/<str:username>', MyJobListView.as_view(), name='my_job_list'),
        path('my/jobs/<int:pk>/update', MyJobUpdateView.as_view(), name='my_job_update'),
        path('my/jobs/<int:pk>/delete', MyJobDeleteView.as_view(), name='my_job_delete'),
        path('my/jobs/public/preview/<str:username>/<int:pk>', MyJobDetailView.as_view(), name='my_job_detail'),
        # path('applicant/<int:user_id>/profile', JobsView.ApplicantDetailView, name='applicant_profile_detail')


    ], 'jobs.views'), namespace='jobs_employer')),

    

]
