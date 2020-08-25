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






    



