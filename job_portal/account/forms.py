from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from account.models import User, Skill, Category, JobseekerProfile, EmployerProfile
from account.models import ( GENDER_CHOICE, EDUCATION_CHOICES, 
                                COMPANY_OWNERSHIP_CHOICES, 
                                JOB_CATEGORY_CHOICES, MARRIED_STATUS_CHOICES, RELIGION_CHOOSE,
                                NATIONALITY_CHOOSE, EDUCATION_BOARD_CHOICES, LANGUAGES_CHOICES )




class JobseekerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        return user


    

class EmployerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        return user




# class JobseekerProfileForm(forms.ModelForm):
    # FirstName = forms.CharField(widget=forms.TextInput(
    #     attrs = {'class': 'form-control', 'placeholder':'enter first name'}
    #     ), required=True, max_length=50)

#     LastName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter last name'}
#         ), required=True, max_length=50)

#     Email = forms.CharField(widget=forms.EmailField(
#         attrs = {'class': 'form-control', 'placeholder':'enter email address'}
#         ), required=True, max_length=50)

#     Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True)

#     DateOfBirth = forms.CharField(widget=forms.DateField(
#         attrs = {'class':'form-control'}
#         ), required=True)

#     MarrigeStatus = forms.ChoiceField(choices=MARRIED_STATUS_CHOICES, required=True)

#     Religion = forms.ChoiceField(choices=RELIGION_CHOOSE, required=True)

#     PhoneNumber = forms.CharField(widget=forms.CharField(
#         attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True)

#     Nationality = forms.ChoiceField(choices=NATIONALITY_CHOOSE, required=True)

#     CurrentAddress = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter current address'}
#         ), required=True, max_length=100)

#     PernamentAddress = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter pernament address'}
#         ), required=True, max_length=100)



#     Religion = forms.ChoiceField(choices=EDUCATION_CHOICES, required=True)

#     EducationProgram = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter education program eg. ComputerScience'}
#         ), required=True, max_length=100)

#     EducationBoard = forms.ChoiceField(choices=EDUCATION_BOARD_CHOICES, required=True)

#     NameOfInstitute = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter education institute name'}
#         ), required=True, max_length=100)


#     MySkill = forms.ModelMultipleChoiceField(Skill.objects.all(), required=False)

#     WorkingExperience = forms.CharField(widget=forms.IntegerField(
#         attrs = {'class': 'form-control'}
#         ), required=False)


#     WorkedCompanyName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter past worked conpany name'}
#         ), required=True, max_length=200)

#     WorkedCompanyWebsite = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com'}
#     ), max_length=100, required=False)


#     JobCategory = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)


#     Language = forms.ChoiceField(choices=LANGUAGES_CHOICES, required=True)

#     AboutMe = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'describe about yourself'}
#     ), required=True, min_length=10)


#     Facebook = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
#     ), max_length=100, required=False)

#     Twitter = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
#     ), max_length=100, required=False)

#     Instagram = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
#     ), max_length=100, required=False)




#     UploadCv = forms.CharField(widget=forms.FileInput(
#         attrs={'class':'form-control', 'placeholder':'upload your cv'}
#     ), required=False)

#     UploadProfilePicture = forms.CharField(widget=forms.ImageField(
#         attrs={'class':'form-control', 'placeholder':'upload your cv'}
#     ), required=False)




#     class Meta():
#         model = JobseekerProfile
#         fields = "__all__"



#     def clean_field(self):
#         data = self.cleaned_data["__all__"]       
#         return data
    
















    




# class EmployerProfileForm(forms.ModelForm):
#     CompanyName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter company name'}
#         ), required=True, max_length=50)

#     CompanyCategory = forms.MultipleChoiceField(required=False)

#     CompanyOwnerShip = forms.ChoiceField(choices=COMPANY_OWNERSHIP_CHOICES, required=True)

#     CompanyWebsite = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com/'}
#     ), max_length=100, required=False)


#     Email = forms.CharField(widget=forms.EmailField(
#         attrs = {'class': 'form-control', 'placeholder':'enter company email address'}
#         ), required=True, max_length=50)

#     Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True)

#     CompanyEstablishDate = forms.CharField(widget=forms.DateField(
#         attrs = {'class':'form-control'}
#         ), required=True)


#     TelNumber = forms.CharField(widget=forms.CharField(
#         attrs = {'class':'form-control', 'placeholder': 'enter company tel. number'}
#         ), max_length=20, required=True)

#     PhoneNumber = forms.CharField(widget=forms.CharField(
#         attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True)


#     ComapnyAddress = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter company address'}
#         ), required=True, max_length=100)


    



#     FirstName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person first name"}
#         ), required=True, max_length=50)

#     LastName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person last name"}
#         ), required=True, max_length=50)


#     Email = forms.CharField(widget=forms.EmailField(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person email address"}
#         ), required=True, max_length=50)

#     PhoneNumber = forms.CharField(widget=forms.CharField(
#         attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True)


#     Facebook = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
#     ), max_length=100, required=False)

#     Twitter = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
#     ), max_length=100, required=False)

#     Instagram = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
#     ), max_length=100, required=False)


#     AboutCompany = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'describe about your company'}
#     ), required=True, min_length=10)


#     UploadCompanyLogo = forms.CharField(widget=forms.ImageField(
#         attrs={'class':'form-control', 'placeholder':'upload your company logo'}
#     ), required=True)



#     class Meta():
#         model = EmployerProfile
#         fields = ['__all__']


#     def clean_field(self):
#         data = self.cleaned_data["__all__"]        
#         return data
    






    



