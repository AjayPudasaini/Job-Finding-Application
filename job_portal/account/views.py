from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, TemplateView


def index(request):
    return render(request, 'base.html')




class JobseekerSignupView(TemplateView):
    template_name = 'register/sign_up.html'


class EmployerSignupView(TemplateView):
    template_name = 'register/sign_up.html'



class LoginView(TemplateView):
    template_name = 'register/login.html'


class BrowseJobView(TemplateView):
    template_name = 'browse_job.html'


# def signup(request):
#     return render(request, 'sign_up.html')