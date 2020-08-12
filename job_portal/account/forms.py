from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from account.models import User, JobseekerProfile, EmployerProfile
from account.models import ( GENDER_CHOICE, EDUCATION_CHOICES, 
                                COMPANY_OWNERSHIP_CHOICES, 
                                JOB_CATEGORY_CHOICES, MARRIED_STATUS_CHOICES, RELIGION_CHOOSE,
                                NATIONALITY_CHOOSE, EDUCATION_BOARD_CHOICES, LANGUAGES_CHOICES )




# Jobseeker Signup Form
class JobseekerSignupForm(UserCreationForm):
    FirstName = forms.CharField(widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder':'enter first name'}
        ), required=True, max_length=50, label='First Name')

    LastName = forms.CharField(widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder':'enter last name'}
        ), required=True, max_length=50, label='Last Name')

    Email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'enter email address'}
        ), required=True, max_length=50, label='Email')

    Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True, label='Gender')

    # MarrigeStatus = forms.ChoiceField(choices=MARRIED_STATUS_CHOICES, required=True, label='Marriage Status')

    # Religion = forms.ChoiceField(choices=RELIGION_CHOOSE, required=True, label='Religion')

    # PhoneNumber = forms.CharField(widget=forms.NumberInput(
    #     attrs={'class':'form-control', 'placeholder': 'enter your personal phone number'}
    #     ), max_length=20, required=True, label='Phone Number')

    # Nationality = forms.ChoiceField(choices=NATIONALITY_CHOOSE, required=True, label='Nationality')

    # CurrentAddress = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder':'enter current address'}
    #     ), required=True, max_length=100, label='Current Address')

    # PernamentAddress = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder':'enter pernament address'}
    #     ), required=True, max_length=100, label='Pernament Address')


    # Education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=True)

    # EducationProgram = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder':'enter education program eg. ComputerScience'}
    #     ), required=True, max_length=100, label='Education Program')

    # EducationBoard = forms.ChoiceField(choices=EDUCATION_BOARD_CHOICES, required=True, label='Education Board')

    # NameOfInstitute = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder':'enter education institute name'}
    #     ), required=True, max_length=100, label='Name Of Institute')


    MySkill = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'enter your skill'}
        ), required=False, label='My Skill')

    # WorkingExperience = forms.IntegerField(max_value=40, min_value=0, label='Working Experience')


    # WorkedCompanyName = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder':'enter past worked conpany name'}
    #     ), required=True, max_length=200, label='Worked Company Name')

    # WorkedCompanyWebsite = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com'}
    # ), max_length=100, required=False, label='Company Website')


    JobCategory = forms.ChoiceField(choices=JOB_CATEGORY_CHOICES, required=False, label='Job Category')


    # Language = forms.ChoiceField(choices=LANGUAGES_CHOICES, required=True, label='Language')

    AboutMe = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'describe about yourself'}
        ), required=True, min_length=10, label='About Me')


    # Facebook = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
    #     ), max_length=100, required=False, label='Facebook')

    # Twitter = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
    #     ), max_length=100, required=False, label='Twitter')

    # Instagram = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
    #     ), max_length=100, required=False, label='Instagram')

    
    class Meta:
        model = User
        fields = ['username', 'FirstName', 'LastName', 'Email','Gender', 'MySkill', 
                 'AboutMe', 'JobCategory']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        jobseekerprofile = JobseekerProfile.objects.create(user=user)
        jobseekerprofile.FirstName = self.cleaned_data.get('FirstName')
        jobseekerprofile.LastName = self.cleaned_data.get('LastName')
        jobseekerprofile.Gender = self.cleaned_data.get('Gender')
        # jobseekerprofile.MarrigeStatus = self.cleaned_data.get('MarrigeStatus')
        # jobseekerprofile.Religion = self.cleaned_data.get('Religion')
        # jobseekerprofile.PhoneNumber = self.cleaned_data.get('PhoneNumber')
        jobseekerprofile.Email = self.cleaned_data.get('Email')
        # jobseekerprofile.Nationality = self.cleaned_data.get('Nationality')
        # jobseekerprofile.CurrentAddress = self.cleaned_data.get('CurrentAddress')
        # jobseekerprofile.PernamentAddress = self.cleaned_data.get('PernamentAddress')
        # jobseekerprofile.Education = self.cleaned_data.get('Education')
        # jobseekerprofile.EducationProgram = self.cleaned_data.get('EducationProgram')
        # jobseekerprofile.EducationBoard = self.cleaned_data.get('EducationBoard')
        # jobseekerprofile.NameOfInstitute = self.cleaned_data.get('NameOfInstitute')
        jobseekerprofile.MySkill = self.cleaned_data.get('MySkill')
        # jobseekerprofile.WorkingExperience = self.cleaned_data.get('WorkingExperience')
        # jobseekerprofile.WorkedField = self.cleaned_data.get('WorkedField')
        # jobseekerprofile.WorkedCompanyName = self.cleaned_data.get('WorkedCompanyName')
        # jobseekerprofile.WorkedCompanyWebsite = self.cleaned_data.get('WorkedCompanyWebsite')
        jobseekerprofile.JobCategory = self.cleaned_data.get('JobCategory')
        # jobseekerprofile.Language = self.cleaned_data.get('Language')
        jobseekerprofile.AboutMe = self.cleaned_data.get('AboutMe')
        # jobseekerprofile.Facebook = self.cleaned_data.get('Facebook')
        # jobseekerprofile.Twitter = self.cleaned_data.get('Twitter')
        # jobseekerprofile.Instagram = self.cleaned_data.get('Instagram')
        jobseekerprofile.save()
        return user




class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username']


class JobseekerProfileUpdateForm(forms.ModelForm):
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

    # CompanyOwnerShip = forms.ChoiceField(choices=COMPANY_OWNERSHIP_CHOICES, required=True)

    CompanyWebsite = forms.CharField(widget=forms.URLInput(
        attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com/'}
        ), max_length=100, required=False)


    Email = forms.CharField(widget=forms.EmailInput(
        attrs = {'class': 'form-control', 'placeholder':'enter company email address'}
        ), required=True, max_length=50)


    # CompanyEstablishDate = forms.CharField(widget=forms.DateInput(
    #     attrs = {'class':'form-control'}
    #     ), required=True)


    # TelNo = forms.CharField(widget=forms.NumberInput(
    #     attrs = {'class':'form-control', 'placeholder': 'enter company tel. number'}
    #     ), max_length=20, required=True)

    # PhoneNumber = forms.CharField(widget=forms.NumberInput(
    #     attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
    #     ), max_length=20, required=True)


    # CompanyAddress = forms.CharField(widget=forms.TextInput(
    #     attrs = {'class': 'form-control', 'placeholder':'enter company address'}
    #     ), required=True, max_length=100)


    



    # FirstName = forms.CharField(widget=forms.TextInput(
    #     attrs = {'class': 'form-control', 'placeholder':"enter company's person first name"}
    #     ), required=True, max_length=50)

    # LastName = forms.CharField(widget=forms.TextInput(
    #     attrs = {'class': 'form-control', 'placeholder':"enter company's person last name"}
    #     ), required=True, max_length=50)


    # Email = forms.CharField(widget=forms.EmailInput(
    #     attrs = {'class': 'form-control', 'placeholder':"enter company's person email address"}
    #     ), required=True, max_length=50)

    # PhoneNumber = forms.CharField(widget=forms.NumberInput(
    #     attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
    #     ), max_length=20, required=True)


    # Facebook = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
    #     ), max_length=100, required=False)

    # Twitter = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
    #     ), max_length=100, required=False)

    # Instagram = forms.CharField(widget=forms.URLInput(
    #     attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
    #     ), max_length=100, required=False)


    AboutCompany = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'describe about your company'}
        ), required=True, min_length=10)


    # CompanyLogo = forms.ImageField(required=True)

    class Meta():
        model = User
        fields = ['username',  'CompanyName', 'CompanyCategory', 'CompanyWebsite', 'Email',
                  'AboutCompany', 'password1', 'password2']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employerprofile = EmployerProfile.objects.create(user=user)
        employerprofile.CompanyName = self.cleaned_data.get('CompanyName')
        employerprofile.CompanyCategory = self.cleaned_data.get('CompanyCategory')
        # employerprofile.CompanyOwnership = self.cleaned_data.get('CompanyOwnership')
        employerprofile.CompanyWebsite = self.cleaned_data.get('CompanyWebsite')
        employerprofile.Email = self.cleaned_data.get('Email')
        # employerprofile.CompanyEstablishDate = self.cleaned_data.get('CompanyEstablishDate')
        employerprofile.AboutCompany = self.cleaned_data.get('AboutCompany')
        # employerprofile.CompanyAddress = self.cleaned_data.get('CompanyAddress')
        # employerprofile.TelNo = self.cleaned_data.get('TelNo')
        # employerprofile.Language = self.cleaned_data.get('Language')
        # employerprofile.AboutMe = self.cleaned_data.get('AboutMe')
        # employerprofile.Facebook = self.cleaned_data.get('Facebook')
        # employerprofile.Twitter = self.cleaned_data.get('Twitter')
        # employerprofile.Instagram = self.cleaned_data.get('Instagram')
        # employerprofile.FirstName = self.cleaned_data.get('FirstName')
        # employerprofile.LastName = self.cleaned_data.get('LastName')
        # employerprofile.PhoneNumber = self.cleaned_data.get('PhoneNumber')
        # employerprofile.Email = self.cleaned_data.get('Email')
        # employerprofile.UploadCv = self.cleaned_data.get('UploadCv')
        employerprofile.save()
        return user




class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'
        exclude = ('user',)









# class JobseekerProfileForm(forms.ModelForm):
#     FirstName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter first name'}
#         ), required=True, max_length=50, label='First Name')

#     LastName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter last name'}
#         ), required=True, max_length=50, label='Last Name')

#     Email = forms.CharField(widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder':'enter email address'}
#         ), required=True, max_length=50, label='Email')

#     Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True, label='Gender')

#     # DateOfBirth = forms.DateField(widget=forms.DateInput(
#     #     attrs = {'class':'form-control',  'placeholder':'Year/Mm/Dd'}
#     #     ), required=True, label='Date Of Birth')

#     MarrigeStatus = forms.ChoiceField(choices=MARRIED_STATUS_CHOICES, required=True, label='Marriage Status')

#     Religion = forms.ChoiceField(choices=RELIGION_CHOOSE, required=True, label='Religion')

#     PhoneNumber = forms.CharField(widget=forms.NumberInput(
#         attrs={'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True, label='Phone Number')

#     Nationality = forms.ChoiceField(choices=NATIONALITY_CHOOSE, required=True, label='Nationality')

#     CurrentAddress = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder':'enter current address'}
#         ), required=True, max_length=100, label='Current Address')

#     PernamentAddress = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder':'enter pernament address'}
#         ), required=True, max_length=100, label='Pernament Address')



#     EducationProgram = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder':'enter education program eg. ComputerScience'}
#         ), required=True, max_length=100, label='Education Program')

#     EducationBoard = forms.ChoiceField(choices=EDUCATION_BOARD_CHOICES, required=True, label='Education Board')

#     NameOfInstitute = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder':'enter education institute name'}
#         ), required=True, max_length=100, label='Name Of Institute')


#     MySkill = forms.ModelMultipleChoiceField(Skill.objects.all(), required=False, label='My Skill')

#     WorkingExperience = forms.IntegerField(max_value=40, min_value=0, label='Working Experience')


#     WorkedCompanyName = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder':'enter past worked conpany name'}
#         ), required=True, max_length=200, label='Worked Company Name')

#     WorkedCompanyWebsite = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com'}
#     ), max_length=100, required=False, label='Company Website')


#     JobCategory = forms.ModelMultipleChoiceField(Category.objects.all(), required=False, label='Job Category')


#     Language = forms.ChoiceField(choices=LANGUAGES_CHOICES, required=True, label='Language')

#     AboutMe = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'describe about yourself'}
#     ), required=True, min_length=10, label='About Me')


#     Facebook = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
#     ), max_length=100, required=False, label='Facebook')

#     Twitter = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
#     ), max_length=100, required=False, label='Twitter')

#     Instagram = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
#     ), max_length=100, required=False, label='Instagram')




#     UploadCv = forms.CharField(widget=forms.FileInput(
#         attrs={'class':'form-control', 'placeholder':'upload your cv'}
#     ), required=False, label='Upload CV')

#     UploadProfilePicture = forms.ImageField(required=True, label='Upload Profile')



#     class Meta:
#         model = JobseekerProfile
#         fields = ['FirstName', 'LastName', 'Email','Gender','DateOffBorth',
#                      'MarrigeStatus', 'Religion', 'PhoneNumber', 'Nationality', 
#                      'CurrentAddress', 'PernamentAddress', 'Religion', 'EducationProgram', 
#                      'EducationBoard', 'NameOfInstitute', 'MySkill', 'WorkingExperience', 
#                      'WorkedCompanyName', 'WorkedCompanyWebsite', 'JobCategory',
#                      'Language', 'AboutMe', 'Facebook', 'Twitter', 'Instagram',
#                      'UploadCv', 'UploadProfilePicture']



#     def clean_field(self):
#         data = self.cleaned_data["__all__"]       
#         return data
    

















    




# class EmployerProfileForm(forms.ModelForm):
#     CompanyName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter company name'}
#         ), required=True, max_length=50)

#     CompanyCategory = forms.ModelMultipleChoiceField(Category.objects.all(),required=False)

#     CompanyOwnerShip = forms.ChoiceField(choices=COMPANY_OWNERSHIP_CHOICES, required=True)

#     CompanyWebsite = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.softwarica.com/'}
#         ), max_length=100, required=False)


#     Email = forms.CharField(widget=forms.EmailInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter company email address'}
#         ), required=True, max_length=50)

#     Gender = forms.ChoiceField(choices=GENDER_CHOICE,  required=True)

#     CompanyEstablishDate = forms.CharField(widget=forms.DateInput(
#         attrs = {'class':'form-control'}
#         ), required=True)


#     TelNo = forms.CharField(widget=forms.NumberInput(
#         attrs = {'class':'form-control', 'placeholder': 'enter company tel. number'}
#         ), max_length=20, required=True)

#     PhoneNumber = forms.CharField(widget=forms.NumberInput(
#         attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True)


#     CompanyAddress = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':'enter company address'}
#         ), required=True, max_length=100)


    



#     FirstName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person first name"}
#         ), required=True, max_length=50)

#     LastName = forms.CharField(widget=forms.TextInput(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person last name"}
#         ), required=True, max_length=50)


#     Email = forms.CharField(widget=forms.EmailInput(
#         attrs = {'class': 'form-control', 'placeholder':"enter company's person email address"}
#         ), required=True, max_length=50)

#     PhoneNumber = forms.CharField(widget=forms.NumberInput(
#         attrs = {'class':'form-control', 'placeholder': 'enter your personal phone number'}
#         ), max_length=20, required=True)


#     Facebook = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.facebook.com/user'}
#         ), max_length=100, required=False)

#     Twitter = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.twitter.com/user'}
#         ), max_length=100, required=False)

#     Instagram = forms.CharField(widget=forms.URLInput(
#         attrs={'class':'form-contol', 'placeholder': 'eg. https://www.instagram.com/user'}
#         ), max_length=100, required=False)


#     AboutCompany = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'describe about your company'}
#         ), required=True, min_length=10)


#     CompanyLogo = forms.ImageField(required=True)



#     class Meta():
#         model = EmployerProfile
#         fields = ['CompanyName', 'CompanyCategory', 'CompanyOwnerShip', 'CompanyWebsite', 'Email',
#                     'Gender', 'CompanyEstablishDate', 'TelNo', 'PhoneNumber',
#                     'CompanyAddress', 'FirstName', 'LastName', 'Email', 'PhoneNumber', 'Facebook',
#                     'Twitter', 'Instagram', 'AboutCompany', 'CompanyLogo']


#     def clean_field(self):
#         data = self.cleaned_data["__all__"]        
#         return data
    


# class SkillForm(forms.ModelForm):
#     class Meta():
#         model = Skill
#         fields = "__all__"


# class CategoryForm(forms.ModelForm):
#     class Meta():
#         model = Category
#         fields = "__all__"






    



