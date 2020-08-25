from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from jobs.forms import job_post_form, JobApplyForm
from account.decorators import jobseeker_required, employer_required
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from jobs.models import JobPost, JobApply
from account.models import User, JobseekerProfile
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from jobs.filers import FilterTime
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages




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


    def get_context_data(self, **kwargs):
        kwargs['post_type'] = 'Post'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator([login_required, employer_required], name='dispatch')
class EmployerDashboard(ListView):
    model = JobPost
    template_name = 'account/Employer/dashboard.html'
    context_object_name = 'mypost'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return JobPost.objects.filter(user=user).order_by('-JobPostDate')






@method_decorator([login_required, employer_required], name='dispatch')
class MyJobDetailView(UserPassesTestMixin, DetailView):
    model = JobPost
    template_name = 'jobs/employer/my_job_detail.html'
    context_object_name = 'mypost'

    def test_func(self):
        jobpost = self.get_object()
        if self.request.user == jobpost.user:
            return True
        return False



 


# Job Updateing Views
@method_decorator([login_required, employer_required], name='dispatch')
class MyJobUpdateView(UserPassesTestMixin, UpdateView):
    model = JobPost
    form_class = job_post_form
    template_name = 'jobs/employer/job_post.html'

    def get_context_data(self, **kwargs):
        kwargs['post_type'] = 'Update'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        jobpost = self.get_object()
        if self.request.user == jobpost.user:
            return True
        return False


# job delete view
@method_decorator([login_required, employer_required], name='dispatch')
class MyJobDeleteView(UserPassesTestMixin, DeleteView):
    model = JobPost
    template_name = 'jobs/employer/my_job_delete.html'
    success_url = '/'

    def test_func(self):
        jobpost = self.get_object()
        if self.request.user == jobpost.user:
            return True
        return False

    

    










def is_valid_queryparm(parm):
    return parm != '' and parm is not None



def BrowseJobView(request):
    jobs = JobPost.objects.all().order_by('-JobPostDate')
    print(jobs)

    # search jobs
    title = request.GET.get('title')
    if is_valid_queryparm(title):
        jobs = jobs.filter(JobTitle__icontains = title)

    location = request.GET.get('location')
    if is_valid_queryparm(location):
        jobs = jobs.filter(Location__icontains = location)

    yourskill = request.GET.get('yourskill')
    if is_valid_queryparm(yourskill):
        jobs = jobs.filter(RequiredSkill__icontains=yourskill)

    # filter jobs
    filter = FilterTime(request.GET, queryset=jobs)
    jobs = filter.qs

    startsalary = request.GET.get('startsalary')
    if is_valid_queryparm(startsalary):
        jobs = jobs.filter(SalaryStart__icontains=startsalary)

    endsalary = request.GET.get('endsalary')
    if is_valid_queryparm(endsalary):
        jobs = jobs.filter(EndSalary__icontains=endsalary)


    paginator = Paginator(jobs, 30, orphans=5)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    contex = {'Jobs':jobs, 'time':filter}
    return render(request, 'jobs/jobseeker/browse_job.html', contex)


def BrowseJobDetail(request, id):
    jobs = JobPost.objects.get(id = id)
    is_SaveJob = False
    if jobs.SaveJob.filter(id=request.user.jobseekerprofile.user_id).exists():
        is_SaveJob = True
    contex = {'mypost':jobs, 'is_save':is_SaveJob}
    return render(request, 'jobs/jobseeker/job_detail.html', contex)


@login_required
@jobseeker_required
def SaveJobs(request, id):
    jobpost = get_object_or_404(JobPost, id=id)
    if jobpost.SaveJob.filter(id=request.user.jobseekerprofile.user_id).exists():
        jobpost.SaveJob.remove(request.user.jobseekerprofile.user_id)
    else:
        jobpost.SaveJob.add(request.user.jobseekerprofile.user_id)
    return redirect('jobs_detail', id) #HttpResponseRedirect(jobpost.get_absolute_url())


@login_required
@jobseeker_required
def ViewSavedJobs(request):
    user = request.user.jobseekerprofile.user_id
    saved_jobs = JobPost.objects.filter(SaveJob=user)
    contex = {'SavedJobs':saved_jobs}
    return render(request, 'jobs/jobseeker/saved_jobs.html', contex)





@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobApplyCreateView(CreateView):
    model = JobApply
    form_class = JobApplyForm
    template_name = 'jobs/jobseeker/job_apply.html'
    context_object_name = 'job'
    # fields = '__all__'


    def get_success_url(self):
        return reverse_lazy('jobs_detail', kwargs={'id': self.kwargs['pk']})

    def form_valid(self, form):
        applicant = JobApply.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['pk'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        form.instance.user = self.request.user
        form.instance.job_id = self.kwargs['pk']
        messages.success(self.request, 'Job has been Applied!')
        print(messages)
        return super().form_valid(form)


@method_decorator([login_required, jobseeker_required], name='dispatch')
class AppliedJobListView(ListView):
    model = JobApply
    template_name = 'jobs/jobseeker/applied_jobs.html'
    context_object_name = 'job'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return JobApply.objects.filter(user = user)
    


@method_decorator([login_required, employer_required], name='dispatch')
class JobAppliedPerson(ListView):
    model = JobApply
    template_name = 'jobs/employer/jobs_applied.html'
    context_object_name = 'jobseeker_applied'


    def get_queryset(self):
        job = get_object_or_404(JobPost, id = self.kwargs.get('id'))
        return JobApply.objects.filter(job = job)
    





def JobseekerProfileView(request):
    jobseeker = JobseekerProfile.objects.all()
    contex = {'jobseeker':jobseeker}
    return render(request, 'jobs/employer/jobseeker_list.html', contex)
