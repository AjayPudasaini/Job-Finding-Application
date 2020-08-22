from django.shortcuts import render, redirect, get_object_or_404
from jobs.forms import job_post_form
from account.decorators import jobseeker_required, employer_required
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from jobs.models import JobPost
from account.models import User
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator






class JobLists(ListView):
    model = JobPost
    template_name = 'account/home.html'
    context_object_name = 'Jobs'
    paginate_by = 20
    ordering = '-JobPostDate'




# For employer's views 


@method_decorator([login_required, employer_required], name='dispatch')
class JobPostCreateView(CreateView):
    model = JobPost
    form_class = job_post_form
    template_name = 'jobs/employer/job_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# @method_decorator([login_required, employer_required], name='dispatch')
# class MyJobListView(ListView):
#     model = JobPost
#     template_name = 'jobs/employer/my_job_list.html'
#     context_object_name = 'mypost'
#     # paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return JobPost.objects.filter(user=user).order_by('-JobPostDate')

@method_decorator([login_required, employer_required], name='dispatch')
class MyJobDetailView(DetailView):
    model = JobPost
    template_name = 'jobs/employer/my_job_detail.html'
    context_object_name = 'mypost'

    


@method_decorator([login_required, employer_required], name='dispatch')
class EmployerDashboard(ListView):
    model = JobPost
    template_name = 'account/Employer/dashboard.html'
    context_object_name = 'mypost'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return JobPost.objects.filter(user=user).order_by('-JobPostDate')




# def MyJobDetailView(request):
#     myjobs = JobPost.objects.filter()





# for Jobseeker

# class BrowseJobView(ListView):
#     model = JobPost
#     template_name = 'jobs/jobseeker/browse_job.html'
#     context_object_name = 'Jobs'
#     paginate_by = 20


def is_valid_queryparm(parm):
    return parm != '' and parm is not None



def BrowseJobView(request):
    jobs = JobPost.objects.all()

    
    contex = {'Jobs':jobs}
    return render(request, 'jobs/jobseeker/browse_job.html', contex)


def BrowseJobDetail(request, id):
    jobs = JobPost.objects.get(id = id)
    contex = {'mypost':jobs}
    return render(request, 'jobs/jobseeker/job_detail.html', contex)
