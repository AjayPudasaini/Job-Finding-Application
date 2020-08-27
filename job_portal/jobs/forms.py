from django import forms
from django.forms import ModelForm
from jobs.models import JobPost, JobApply
from account.models import(JOB_CATEGORY_CHOICES, EDUCATION_CHOICES)
from jobs.models import (LOCATION_CHOOSE, WORKING_SHIFTS, Job_Level_Choices,
                        JOB_AVALIABLE_TIME, Gender)

from django.contrib.admin import widgets



class job_post_form(forms.ModelForm):
    JobTitle = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Graphic Designer, Web Developer'}
    ), max_length=500,  required=True, label='Job Title')
    Location = forms.ChoiceField(choices=LOCATION_CHOOSE, required=True, label='Job Location')
    NumberOfVacancies = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Number Of Vacancies eg: 1'}
        ), min_value=0, required=True, label='Number Of Vanacnies')

    SalaryStart = forms.FloatField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder': 'Salary start with in rs'}
    ), min_value=0, required=False, label='Start Salary')

    EndSalary = forms.FloatField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder': 'Salary end with in rs'}
    ), min_value=0, required=False, label='End Salary')

    RequiredSkill = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Adobe Photoshop, Adobe InDesign'}
    ), max_length=500,  required=True, label='Required Skill Ofr This Job', help_text='seprate with comma","')

    JobLevel = forms.ChoiceField(choices=Job_Level_Choices, required=True, label='Job Level')
    AvaliableTime = forms.ChoiceField(choices=JOB_AVALIABLE_TIME, required=True, label='Avaliable Time')
    JobShift = forms.ChoiceField(choices=WORKING_SHIFTS, required=True, label='Job Shift')
    RequiredEducation = forms.ChoiceField(choices=EDUCATION_CHOICES, required=True, label='Required Education')
    RequiredExperience = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'required experince for thus job'}
    ), min_value=0, help_text='Experience in year', required=True, label='Required Experience')
    JobCategory = forms.ChoiceField(choices=JOB_CATEGORY_CHOICES, required=True, label='Job Category')
    Gender = forms.ChoiceField(choices=Gender, required=True)

    HiringBanner = forms.ImageField(required=False, label='Your Company Banner')

    JobExpiryDate = forms.DateTimeField( help_text= 'Note* format YY-MM-DD H:M:S', widget=forms.DateTimeInput(
        attrs={'class':'form-control', 'placeholder':"Date and Time Format: YY-MM-DD H:M:S"}
    ), input_formats=['%Y-%m-%d %H:%M:%S'], label='Job Expery Date') 






    class Meta():
        model = JobPost
        fields = ['JobTitle','Location', 'NumberOfVacancies', 'SalaryStart',  
                    'EndSalary', 'RequiredExperience',  'JobLevel', 'AvaliableTime', 'RequiredSkill', 
                    'JobShift', 'RequiredEducation', 'RequiredExperience', 'JobCategory', 
                    'Gender', 'JobDescreptions', 'JobSpecification', 'HiringBanner', 'JobExpiryDate']



    

class JobApplyForm(forms.ModelForm):
    # JobApplyReason = forms.CharField(widget=forms.Textarea(), label='Why you choose this job')
    class Meta():
        model = JobApply
        fields = ['JobApplyReason']

    widgets
    


    
