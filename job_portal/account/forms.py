from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from account.models import User, JobseekerProfile, EmployerProfile
from account.models import ( GENDER_CHOICE, EDUCATION_CHOICES, 
                                COMPANY_OWNERSHIP_CHOICES, 
                                JOB_CATEGORY_CHOICES, MARRIED_STATUS_CHOICES, RELIGION_CHOOSE,
                                NATIONALITY_CHOOSE, EDUCATION_BOARD_CHOICES, LANGUAGES_CHOICES )


from ckeditor.widgets import CKEditorWidget
from django.contrib import messages
from django.shortcuts import HttpResponse
import os

# Jobseeker Signup Form
class JobseekerSignupForm(UserCreationForm):
    FirstName = forms.CharField(widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder':'enter first name'}
        ), required=True, max_length=50, label='First Name')

    LastName = forms.CharField(widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder':'enter last name'}
        ), required=True, max_length=50, label='Last Name')

    Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True, label='Gender')


    JobCategory = forms.ChoiceField(choices=JOB_CATEGORY_CHOICES, required=False, label='Job Category')


    AboutMe = forms.CharField(widget=CKEditorWidget(
        attrs={'class': 'form-control', 'placeholder': 'describe about yourself'}
        ),label='About Me')



    class Meta:
        model = User
        fields = ['username', 'email', 'FirstName', 'LastName', 'Gender', 
                 'AboutMe', 'JobCategory']


    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email


    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username and User.objects.filter(username=username).exclude(email=email).count():
            raise forms.ValidationError('This username has already been taken!')
        return username


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        jobseekerprofile = JobseekerProfile.objects.create(user=user)
        jobseekerprofile.FirstName = self.cleaned_data.get('FirstName')
        jobseekerprofile.LastName = self.cleaned_data.get('LastName')
        jobseekerprofile.Gender = self.cleaned_data.get('Gender')
        jobseekerprofile.MySkill = self.cleaned_data.get('MySkill')
        jobseekerprofile.JobCategory = self.cleaned_data.get('JobCategory')
        jobseekerprofile.AboutMe = self.cleaned_data.get('AboutMe')
        jobseekerprofile.save()
        return user




class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'email']


class JobseekerProfileUpdateForm(forms.ModelForm):
    ProfileImage = forms.ImageField(help_text='Only supports .png, .jpg, .jpeg', widget=forms.FileInput(
        attrs={'class':'form-control'}), label='Upload Your CV')
    UploadCv = forms.FileField(help_text='Only supports .pdf, .doc, .docx', widget=forms.FileInput(
        attrs={'class':'form-control'}), label='Upload Your CV')
    class Meta():
        model = JobseekerProfile
        fields = '__all__'
        exclude = ('user',)


# Employer Signup Form
class EmployerSignupForm(UserCreationForm):
    CompanyName = forms.CharField(widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder':'enter company name'}
        ), required=True, max_length=50)

    CompanyCategory = forms.ChoiceField(choices=JOB_CATEGORY_CHOICES ,required=False)


    CompanyWebsite = forms.CharField(widget=forms.URLInput(
        attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com/'}
        ), max_length=100, required=False)



    AboutCompany = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'describe about your company'}
        ), required=True, min_length=10)


    class Meta():
        model = User
        fields = ['username', 'email', 'CompanyName', 'CompanyCategory', 'CompanyWebsite', 
                  'AboutCompany', 'password1', 'password2']



    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email


    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username and User.objects.filter(username=username).exclude(email=email).count():
            raise forms.ValidationError('This username has already been taken!')
        return username


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employerprofile = EmployerProfile.objects.create(user=user)
        employerprofile.CompanyName = self.cleaned_data.get('CompanyName')
        employerprofile.CompanyCategory = self.cleaned_data.get('CompanyCategory')
        employerprofile.CompanyWebsite = self.cleaned_data.get('CompanyWebsite')
        employerprofile.AboutCompany = self.cleaned_data.get('AboutCompany')
        employerprofile.save()
        return user




class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'
        exclude = ('user',)





