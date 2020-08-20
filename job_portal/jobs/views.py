from django.shortcuts import render, redirect
from jobs.forms import job_post_form
from account.decorators import jobseeker_required, employer_required
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView
from jobs.models import JobPost

# Create your views here
# 
# For employer's views 

# def job_post_view(request):
#     form = job_post_form()
#     contex = {'form':form}
#     return render (request, 'jobs/employer/job_post.html', contex)


class JobPostCreateView(CreateView):
    model = JobPost
    form_class = job_post_form
    template_name = 'jobs/employer/job_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class my_job_post_view(TemplateView):
    template_name = 'jobs/employer/my_job_list.html'