from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView
from account.models import User, EmployerProfile, JobseekerProfile, Skill, Category
from account.forms import (JobseekerSignupForm, EmployerSignupForm, JobseekerProfileForm, 
                            EmployerProfileForm, SkillForm, CategoryForm, JobseekerUpdateForm)
from django.contrib.auth import login,authenticate
from account.decorators import jobseeker_required, employer_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    if request.user.is_authenticated:
        if request.user.is_jobseeker:
            return redirect('jobseeker:jobseeker_dashboard')
        else:
            return redirect('employer:employer_profile')
    else:
        return render(request, 'account/home.html')



# Jobseeker Signup

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
        return redirect('jobseeker:jobseeker_dashboard')



# Employer Signup 

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




# Employer Profiles

@method_decorator([login_required, employer_required], name='dispatch')
class EmployerProfileView(TemplateView):
    template_name = 'account/Employer/profile.html'





# Jobseeker profiles

@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobseekerDashboardView(TemplateView):
    template_name = 'account/Jobseeker/dashboard.html'


@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobseekerProfileDetailView(ListView):
    model = JobseekerProfile
    template_name = 'account/Jobseeker/profile_detail.html'
    context_object_name = 'profile'

    def get_queryset(self):
        queryset = self.request.user.user
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return User.objects.filter(user=user)




@method_decorator([login_required, jobseeker_required], name='dispatch')
class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'account/Jobseeker/add_skill.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   

@method_decorator([login_required, jobseeker_required], name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'account/Jobseeker/add_category.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        

# @method_decorator([login_required, jobseeker_required], name='dispatch')
# class JobseekerProfileCreateView(CreateView):
#     model = JobseekerProfile
#     form_class = JobseekerProfileForm
#     template_name = 'account/Jobseeker/add_profile_detail.html'

#     def form_valid(self, form):
#         profile = form.save(commit = False)
#         profile.user = self.request.user
#         profile.save()
#         messages.success(self.request, 'Account have been updated')
#         # form.instance.user = self.request.user
#         # return super().form_valid(form)


@login_required
@jobseeker_required
def JobseekerProfileCreateView(request):
    if request.method == 'POST':
        username_form = JobseekerUpdateForm(request.POST, instance=request.user)
        profile_form = JobseekerProfileForm(request.POST, request.FILES, instance = request.user)

        if username_form.is_valid() and profile_form.is_valid():
            username_form.save()
            profile_form.save()

            messages.success(request, f'Your Accounted has been updated!')
            return redirect('jobseeker:jobseeker_profile_detail')

    else:
        username_form = JobseekerUpdateForm(request.POST, instance=request.user)
        profile_form = JobseekerProfileForm(request.POST, request.FILES, instance = request.user)

    contex = {'u_form': username_form, 'p_form': profile_form }
    return render(request, 'account/Jobseeker/add_profile_detail.html' , contex) 




@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobseekerProfileView(TemplateView):
    template_name = 'account/Jobseeker/profile.html'




@method_decorator([login_required, jobseeker_required], name='dispatch')
class BrowseJobView(TemplateView):
    template_name = 'browse_job.html'





@login_required
def delete_acccount(request, id):
    uff = User.objects.get(id=id)
    if request.method == 'POST':
        uff.delete()
        return redirect('../') 
    contex = {'uff':uff}  
    return render(request, 'account/delete_account.html', contex)




















