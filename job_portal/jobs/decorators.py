from account.models import JobseekerProfile, EmployerProfile
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


def complete_profile_required(view_func):
    def wrapper_func(request, *args, **Kwargs):
        if request.user.jobseekerprofile.percentage_complete == 100:
            return view_func(request, *args, **Kwargs)          
        else:
            # raise PermissionDenied
            messages.warning(request, 'Please Complete your profile first, and then apply job! Note*: All profile fields have value')
            return redirect('jobseeker:jobseeker_profile_add_detail')
            
            # return HttpResponse('<script>alert("Your profile has not complete, please complete your profile first ")</script>')            
    return wrapper_func


def complete_employer_profile(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.employerrprofile.Company_percentage_complete == 100:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request,  f'Please first Complete your company profile first, and then post job! Note*: All profile fields have value')
            return redirect('employer:employer_profile_update_detail')
            # return HttpResponse('<script>alert("Your profile has not complete, please complete your profile first ")</script>')   

    return wrapper_func         