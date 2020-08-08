from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from account.models import User, EmployerProfile, JobseekerProfile
from account.forms import JobseekerSignupForm, EmployerSignupForm
from django.contrib.auth import login,authenticate
from account.decorators import jobseeker_required, employer_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        if request.user.is_jobseeker:
            return redirect('jobseeker:jobseeker_profile')
        else:
            return redirect('employer:employer_profile')
    else:
        return render(request, 'account/home.html')




class JobseekerSignupView(CreateView):
    model = User
    form_class = JobseekerSignupForm
    template_name = 'register/sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Jobseeker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('jobseeker:jobseeker_profile')



class EmployerSignupView(CreateView):
    model = User
    form_class = EmployerSignupForm
    template_name = 'register/sign_up.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('employer:employer_profile')




@method_decorator([login_required, employer_required], name='dispatch')
class EmployerProfileView(TemplateView):
    template_name = 'account/Employer/profile.html'

@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobseekerProfileView(TemplateView):
    template_name = 'account/Jobseeker/profile.html'



# class LoginView(TemplateView):
#     template_name = 'register/login.html'

@method_decorator([login_required, jobseeker_required], name='dispatch')
class BrowseJobView(TemplateView):
    template_name = 'browse_job.html'


# def signup(request):
#     return render(request, 'sign_up.html')