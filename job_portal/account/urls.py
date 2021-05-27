from django.urls import path, include
from account import views
from account.views import (JobseekerSignupView, EmployerSignupView, 
                             JobseekerProfileUpdateView, EmoloyerProfileDetailView,
                             JobseekerProfileDetailView)

from jobs.views import (EmployerDashboard)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('over', views.index, name = 'index'),
    path('account/jobseeker/register', JobseekerSignupView.as_view(), name = 'register-jobseeker'),
    path('account/employer/register', EmployerSignupView.as_view(), name = 'register-employer'),
    path('register-as', views.register_as, name = 'register_as'),

    path('jobseeker/', include(([
        path('profile/detail/<int:user_id>', JobseekerProfileDetailView.as_view(), name = 'jobseeker_profile_detail'),
        path('profile/update/detail', views.JobseekerProfileUpdateView, name = 'jobseeker_profile_add_detail'),
        path('profile/settings', views.JobseekerSetting, name = 'jobseeker_profile_setting'),
        path('profile/change/password', views.JobseekerChangePassword, name = 'jobseeker_change_password'),
    ], 'account.views' ), namespace='jobseeker')),


    path('employer/', include(([
        path('dashboard/<str:username>', EmployerDashboard.as_view(), name = 'employer_dashboard'),
        path('profile/detail/<int:user_id>', EmoloyerProfileDetailView.as_view(), name = 'employer_profile_detail'),
        path('profile/update/detail/', views.EmployerProfileUpdateView, name = 'employer_profile_update_detail'),
        path('profile/settings', views.EmployerSettings, name = 'employer_settings'),
        path('profile/change/password', views.EmployerPasswordChange, name = 'employer_change_password')
    ], 'account.views' ), namespace='employer')),
    
    path('login', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='register/passwords/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='register/passwords/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='register/passwords/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-reset', auth_views.PasswordResetCompleteView.as_view(template_name='register/passwords/password_reset_complete.html'), name='password_reset_complete'),
    path('delete/account/<int:id>', views.delete_acccount, name='delete_account')

]
