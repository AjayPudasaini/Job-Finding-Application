from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView
from account.models import User, EmployerProfile, JobseekerProfile
from account.forms import (JobseekerSignupForm, EmployerSignupForm, JobseekerProfileUpdateForm, UserUpdateForm, EmployerProfileUpdateForm)
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
            return redirect('employer:employer_dashboard')
    else:
        return render(request, 'account/home.html')



# Jobseeker Signup

class JobseekerSignupView(CreateView):
    model = User
    form_class = JobseekerSignupForm
    template_name = 'register/sign_up.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
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
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('employer:employer_dashboard')




# Employer Profiling

@method_decorator([login_required, employer_required], name='dispatch')
class EmployerProfileView(TemplateView):
    template_name = 'account/Employer/dashboard.html'




@login_required
@employer_required
def EmployerProfileDetailView(request, user_id):
    detail = EmployerProfile.objects.filter(user_id=user_id)
    contex = {'profile':detail}
    return render(request, 'account/Employer/employer_profile_detail.html', contex)




@login_required
@employer_required
def EmployerProfileUpdateView(request):
    if request.method == 'POST':
        profile_form = EmployerProfileUpdateForm(request.POST, request.FILES, instance=request.user.employerrprofile)
        if profile_form.is_valid():
            request.user.username = request.POST['username']
            request.user.save()
            profile_form.save()

            messages.success(request, f'Your Accounted has been updated!')
            return redirect('/')

    else:
        username_form = UserUpdateForm(instance=request.user)
        profile_form = EmployerProfileUpdateForm(instance=request.user.employerrprofile)

    contex = {'u_form': username_form, 'p_form': profile_form }
    return render(request, 'account/Employer/update_profile_detail.html' , contex)


# @login_required
# @employer_required
# def EmployerProfileCreateView(request, user_id):
#     instance = EmployerProfile.objects.get(user_id = user_id)
#     if request.method == 'POST':
#         employer_profile_form = EmployerProfileForm(request.POST, request.FILES, instance=instance)
#         if employer_profile_form.is_valid():
#             employer_profile_form.save()
#             messages.success(request, 'Employer profile has been updated')
#             return redirect('employer:employer_profile_detail', user_id = user_id )
#     else:
#         employer_profile_form = EmployerProfileForm(instance=instance)
#     contex = {'profile':employer_profile_form}
#     return render(request, 'account/Employer/update_profile_detail.html', contex)
    






# Jobseeker Profiling

@method_decorator([login_required, jobseeker_required], name='dispatch')
class JobseekerDashboardView(TemplateView):
    template_name = 'account/Jobseeker/dashboard.html'



@login_required
@jobseeker_required
def JobseekerProfileDetailView(request, user_id):
    detail = JobseekerProfile.objects.filter(user_id=user_id)
    contex = {'profile':detail}
    return render(request, 'account/Jobseeker/profile_detail.html', contex)




# @method_decorator([login_required, jobseeker_required], name='dispatch')
# class JobseekerProfileCreateView(CreateView):
#     model = JobseekerProfile
#     form_class = JobseekerProfileUpdateForm
#     template_name = 'account/Jobseeker/add_profile_detail.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)





        

# @login_required
# @jobseeker_required
# def JobseekerProfileUpdateView(request, user_id):
#     # instance = JobseekerProfile.objects.get(user_id=user_id)
#     if request.method == 'POST':
#         profile_form = JobseekerProfileUpdateForm(request.POST, request.FILES, instance=instance)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, f'Your Accounted has been updated!')
#             return redirect('jobseeker:jobseeker_profile_detail', user_id=user_id)
#         else:
#             messages.error(request, f'Your Accounted has not updated!')
#     else:
#         profile_form = JobseekerProfileForm(request.POST, request.FILES, instance=instance)
#     contex = {'profile_form': profile_form }
#     return render(request, 'account/Jobseeker/edit.html', contex) 


@login_required
@jobseeker_required
def JobseekerProfileUpdateView(request):
    if request.method == 'POST':
        profile_form = JobseekerProfileUpdateForm(request.POST, request.FILES, instance=request.user.jobseekerprofile)
        if profile_form.is_valid():
            request.user.username = request.POST['username']
            request.user.save()
            profile_form.save()

            messages.success(request, f'Your Accounted has been updated!')
            return redirect('/')

    else:
        username_form = UserUpdateForm(instance=request.user)
        profile_form = JobseekerProfileUpdateForm(instance=request.user.jobseekerprofile)

    contex = {'u_form': username_form, 'p_form': profile_form }
    return render(request, 'account/Jobseeker/add_profile_detail.html' , contex)






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




















