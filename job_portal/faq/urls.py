from django.urls import path, include
from faq import views
from faq.views import FaqForJobseekerListView, FaqForJobseekerDetailView, FaqForEmployerListView, FaqForEmployerDetailView

urlpatterns = [
    path('jobseeker/', include(([
        path('faq/list', FaqForJobseekerListView.as_view(), name = 'jobseeker_faq_list'),
        path('faq/detail/<int:pk>',FaqForJobseekerDetailView.as_view(), name = 'jobseeker_faq_detail'),
    ], 'faq.views' ), namespace='jobseeker_faq')),

    path('employer/', include(([
        path('faq/list', FaqForEmployerListView.as_view(), name = 'employer_faq_list'),
        path('faq/detail/<int:pk>',FaqForEmployerDetailView.as_view(), name = 'employer_faq_detail'),
    ], 'faq.views' ), namespace='employer_faq')),
]
