from django.urls import path, include
from account import views
from account.views import JobseekerSignupView, EmployerSignupView, LoginView, BrowseJobView



urlpatterns = [
    path('', views.index, name = 'index'),
    path('account/jobseeker/register', JobseekerSignupView.as_view(), name = 'register-jobseeker'),
    path('account/employer/register', EmployerSignupView.as_view(), name = 'register-employer'),
    path('account/login', LoginView.as_view(), name = 'login'),
    path('browse/jobs', BrowseJobView.as_view(), name = 'browse_job')
]
