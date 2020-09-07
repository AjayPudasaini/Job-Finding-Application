from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView, DetailView
from account.models import User, EmployerProfile, JobseekerProfile
from account.forms import (JobseekerSignupForm, EmployerSignupForm, JobseekerProfileUpdateForm, UserUpdateForm, EmployerProfileUpdateForm)
from django.contrib.auth import login,authenticate, update_session_auth_hash
from account.decorators import jobseeker_required, employer_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from jobs.models import JobPost



def index(request):
    if request.user.is_authenticated:
        if request.user.is_jobseeker:
            return redirect('homes')
        else:
            return redirect('employer:employer_dashboard', username=request.user.username)
    else:
        return render(request, 'account/home.html')


def register_as(request):
    return render(request, 'register/register_as.html')

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
        return redirect('homes')



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
        return redirect('employer:employer_dashboard', username=request.user.username)



class EmoloyerProfileDetailView(DetailView):
    model = EmployerProfile
    context_object_name = 'profile'
    template_name = 'account/Employer/employer_profile_detail.html'
    pk_url_kwarg = 'user_id'



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
            return redirect('employer:employer_dashboard', username=request.user.username)

    else:
        username_form = UserUpdateForm(instance=request.user)
        profile_form = EmployerProfileUpdateForm(instance=request.user.employerrprofile)

    contex = {'u_form': username_form, 'p_form': profile_form }
    return render(request, 'account/Employer/update_profile_detail.html' , contex)



@login_required
@employer_required
def EmployerSettings(request):
    return render(request, 'account/Employer/settings.html')


@login_required
@employer_required
def EmployerPasswordChange(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')

        else:
            form = PasswordChangeForm(request.user)
    contex = {'form':form}
    return render(request, 'account/Employer/change_password.html', contex)


class JobseekerProfileDetailView(DetailView):
    model = JobseekerProfile
    context_object_name = 'profile'
    template_name = 'account/Jobseeker/profile_detail.html'
    pk_url_kwarg = 'user_id'


@login_required
@jobseeker_required
def JobseekerProfileUpdateView(request):
    if request.method == 'POST':
        username_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = JobseekerProfileUpdateForm(request.POST, request.FILES, instance=request.user.jobseekerprofile)
        if profile_form.is_valid() and username_form.is_valid():
            # request.user.username = request.POST['username']
            # request.user.save()
            username_form.save()
            profile_form.save()

            messages.success(request, f'Your Accounted has been updated!')
            return redirect('/')
        messages.error(request, f'your profile has not updated')

    else:
        username_form = UserUpdateForm(instance=request.user)
        profile_form = JobseekerProfileUpdateForm(instance=request.user.jobseekerprofile)

    contex = {'u_form': username_form, 'p_form': profile_form }
    return render(request, 'account/Jobseeker/add_profile_detail.html' , contex)








@login_required
@jobseeker_required
def JobseekerSetting(request):
    return render(request, 'account/Jobseeker/settings.html')


@login_required
@jobseeker_required
def JobseekerChangePassword(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
        else:
            form = PasswordChangeForm(request.user)
    contex = {'form':form}
    return render(request, 'account/Jobseeker/change_password.html', contex)








#  Both account delete
@login_required
def delete_acccount(request, id):
    uff = User.objects.get(id=id)
    if request.method == 'POST':
        uff.delete()
        return redirect('../') 
    contex = {'uff':uff}  
    return render(request, 'account/delete_account.html', contex)




















