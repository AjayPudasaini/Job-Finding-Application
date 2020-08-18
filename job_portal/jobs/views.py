from django.shortcuts import render, redirect
from jobs.forms import job_post_form
from account.decorators import jobseeker_required, employer_required
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView

# Create your views here
# 
# For employer's views 

def job_post_view(request):
    form = job_post_form()
    contex = {'form':form}
    return render (request, 'jobs/employer/job_post.html', contex)



class my_job_post_view(TemplateView):
    template_name = 'jobs/employer/my_job_list.html'