from django.urls import path, include
from account import views
from account.views import JobseekerSignupView, EmployerSignupView, BrowseJobView, JobseekerProfileView, EmployerProfileView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('browse/jobs', BrowseJobView.as_view(), name = 'browse_job'),
    path('account/jobseeker/register', JobseekerSignupView.as_view(), name = 'register-jobseeker'),
    path('account/employer/register', EmployerSignupView.as_view(), name = 'register-employer'),

    path('jobseeker/', include(([
        path('profile', JobseekerProfileView.as_view(), name = 'jobseeker_profile'),
    ], 'account.views' ), namespace='jobseeker')),

    path('employer/', include(([
        path('profile', EmployerProfileView.as_view(), name = 'employer_profile'),
    ], 'account.views' ), namespace='employer')),
    
    path('login', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
]
