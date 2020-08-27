from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from PIL import Image
from django.urls import reverse
from django.core import validators
from account.validators import validate_cv_extension, Validate_image_extension



GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'
GENDER_CHOICE = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)


MARRIED_STATUS_SINGLE = 'Single'
MARRIED_STATUS_MARRIED = 'Married'
MARRIED_STATUS_CHOICES = (
    (MARRIED_STATUS_SINGLE, 'Single'),
    (MARRIED_STATUS_MARRIED, 'Married'),
)


EDUCATION_INTERMIDATE = 'Intermidate Level Complete'
EDUCATION_BACHOLERS_RUNNING_OR_COMPLETE = 'Bacholer Running/Complete'
EDUCATION_MASTER_RUNNING_OR_COMPLETE = 'Master Running/Complete'
EDUCATION_PHD = 'Ph. D. Running/Complete'
EDUCATION_OTHER = 'OTHER'

EDUCATION_CHOICES = (
    (EDUCATION_INTERMIDATE, 'Intermidate Level Complete'),
    (EDUCATION_BACHOLERS_RUNNING_OR_COMPLETE, 'Bacholer Running/Complete'),
    (EDUCATION_MASTER_RUNNING_OR_COMPLETE, 'Master Running/Complete'),
    (EDUCATION_PHD, 'Ph. D. Running/Complete'),
    (EDUCATION_OTHER, 'OTHER'),
)



JOB_CATEGORY_CHOICES = (
    ('Architecture/Interior Designing', 'Architecture/Interior Designing'),
    ('Construction/Engineering', 'Construction/Engineering'),
    ('Commercial/Logistics', 'Commercial/Logistics'),
    ('Creative/Graphic/Designing', 'Creative/Graphic/Designing'),
    ('Hospilaty', 'Hospilaty'),
    ('NGO/INGO/Social Work', 'NGO/INGO/Social Work'),
    ('Techng/Education', 'Techng/Education'),
    ('General MGMT./Administration/Operations', 'General MGMT./Administration/Operations'),
    ('Healthcare/Pharma/Biotech/Medical', 'Healthcare/Pharma/Biotech/Medical'),
    ('Human Resources/ Org.Development', 'Human Resources/ Org.Development'),
    ('Sales/Public Relations', 'Sales/Public Relations'),
    ('Research and Development', 'Research and Development'),
    ('Production/Maintenance/Quality', 'Production/Maintenance/Quality'),
    ('Marketing/Advertisement/Custom service', 'Marketing/Advertisement/Custom service'),
    ('Legal Services', 'Legal Services'),
    ('Accounting/Finance', 'Accounting/Finance'),
    ('Banking/Insurance/Finance Services', 'Banking/Insurance/Finance Services'),
    ('Fashion/Textile Designing', 'Fashion/Textile Designing'),
    ('Secretarial/Front Office/Data Entry', 'Secretarial/Front Office/Data Entry'),
    ('IT & Telecommunication', 'IT & Telecommunication'),
    ('Productive/Securaty Service', 'Productive/Securaty Service'),
    ('Journalism/Editor/Media', 'Journalism/Editor/Media'),
    ('Others', 'Others'),
)


RELIGION_CHOOSE = (
    ('Hinduism', 'Hinduism'),
    ('Buddhism', 'Buddhism'),
    ('Christianity', 'Christianity'),
    ('Islam', 'Islam'),
    ('Sikhism', 'Sikhism'),
    ('Jainism', 'Jainism'),
    ('Others', 'Others'),
)

NATIONALITY_CHOOSE = (
    ('Nepali', 'Nepali'),
    ('Indian', 'Indian'),
    ('Chineases', 'Chineases'),
    ('Others', 'Others'),
)

EDUCATION_BOARD_CHOICES = (
    ('NEB', 'NEB'),
    ('Tribhuvan Univercity', 'Tribhuvan Univercity'),
    ('Mid-Westran Univercity', 'Mid-Westran Univercity'),
    ('Architure and Forestry Univercity', 'Architure and Forestry Univercity'),
    ('Nepal Open Univercity', 'Nepal Open Univercity'),
    ('Pokhara Univercity', 'Pokhara Univercity'),
    ('Nepal Sanskrit Univercity', 'Nepal Sanskrit Univercity'),
    ('Lumbini Buddhist Univercity', 'Lumbini Buddhist Univercity'),
    ('Far-Western Univercity', 'Far-Western Univercity'),
    ('Kathmandu Univercity', 'Kathmandu Univercity'),
    ('Purbanchal Univercity', 'Purbanchal Univercity'),
    ('Others', 'Others'), 
)


LANGUAGES_CHOICES = (
    ('Nepali', 'Nepali'),
    ('English', 'English'),
    ('Others', 'Others'),  
)

COMPANY_OWNERSHIP_CHOICES = (
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Government', 'Government'),
    ('Others', 'Others'),

)





class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    email = models.CharField(max_length=256, verbose_name='Email')




class JobseekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name='jobseekerprofile')

    # Basic Information
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    Gender = models.CharField(max_length=20,blank=False, choices=GENDER_CHOICE)
    MarrigeStatus = models.CharField(max_length=20, blank=True, choices=MARRIED_STATUS_CHOICES, verbose_name='Marrige Status')
    Religion = models.CharField(max_length=20, blank=True, choices=RELIGION_CHOOSE)
    PhoneNumber = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    Nationality = models.CharField(max_length=30, blank=True, choices=NATIONALITY_CHOOSE, verbose_name='Nationality')
    CurrentAddress = models.CharField(max_length=100, blank=True, verbose_name='Current Address')
    PernamentAddress = models.CharField(max_length=100, blank=True, verbose_name='Pernament Address')
    ProfileImage = models.ImageField(default='defaultusers.png', blank=True, upload_to='Jobseeker/Profile_Pictures', verbose_name='Profile Picture', validators=[Validate_image_extension])
   
    # Education Information
    Education = models.CharField(max_length=100, blank=True, choices=EDUCATION_CHOICES, verbose_name='Education')
    EducationProgram = models.CharField(max_length=200, blank=True, verbose_name='Education Program')
    EducationBoard = models.CharField(max_length=100, blank=True, choices=EDUCATION_BOARD_CHOICES, verbose_name='Education Board')
    NameOfInstitute = models.CharField(max_length=200, blank=True, verbose_name='Name Of Institute')

    # skill
    MySkill = models.CharField(max_length=250, blank=True, verbose_name='My Skill', null=True)

    # Past jobs
    WorkingExperience = models.IntegerField(default=0, blank=True, verbose_name='Working Experience') 
    WorkedField = models.CharField(max_length=50, null=True, blank=True, verbose_name='Worked Related Fields')  
    WorkedCompanyName = models.CharField(max_length=200, blank=True, verbose_name='Worked Company Name')
    WorkedCompanyWebsite = models.URLField(max_length=200, blank=True, verbose_name='Worked Company Website')

    # job category
    JobCategory = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES, verbose_name='Job Category')

    # add language
    Language = models.CharField(max_length=20, blank=True, choices=LANGUAGES_CHOICES)

    # about Me
    AboutMe = RichTextField(verbose_name='About Me')

    # Social account
    Facebook = models.URLField(max_length=100, blank=True,)
    Twitter = models.URLField(max_length=100, blank=True,)
    Instagram = models.URLField(max_length=100, blank=True,)

    # upload cv
    UploadCv = models.FileField(upload_to='Jobseeker/CVs',null=True, blank=True, validators=[validate_cv_extension],  verbose_name='Upload Your CV')





    def __str__(self):
        return f'{self.user.username} profile'

    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ProfilePic = Image.open(self.ProfileImage.path)
        if ProfilePic.height>300 or ProfilePic.width>300:
            output_size = (300, 300)
            ProfilePic.thumbnail(output_size)
            ProfilePic.save(self.ProfileImage.path)



    @property 
    def percentage_complete(self):
        percent = { 'FirstName': 1, 'LastName': 1,
                     'Gender': 1, 'MarrigeStatus':1,
                     'Religion':1, 'PhoneNumber':3,
                     'Nationality':1, 'CurrentAddress':3,
                     'PernamentAddress':3, 'ProfileImage':5,
                     'Education':5, 'EducationProgram':5,
                     'EducationBoard':5, 'NameOfInstitute':5,
                     'MySkill':5, 'WorkingExperience':2,
                     'WorkedField':3, 'WorkedCompanyName': 3,
                     'WorkedCompanyWebsite':3, 'JobCategory':4,
                     'Language':2, 'AboutMe': 10,
                     'Facebook':1, 'Twitter':1, 'Instagram':1,
                     'UploadCv':20}
        total = 0
        if self.FirstName:
            total += percent.get('FirstName', 0)
        if self.LastName:
            total += percent.get('LastName', 0)

        if self.Gender:
            total += percent.get('Gender', 0)

        if self.MarrigeStatus:
            total += percent.get('MarrigeStatus', 0)

        if self.Religion:
            total += percent.get('Religion', 0)

        if self.PhoneNumber:
            total += percent.get('PhoneNumber', 0)

        if self.Nationality:
            total += percent.get('Nationality', 0)

        if self.CurrentAddress:
            total += percent.get('CurrentAddress', 0)

        if self.PernamentAddress:
            total += percent.get('PernamentAddress', 0)

        if self.ProfileImage:
            total += percent.get('ProfileImage', 0)

        if self.Education:
            total += percent.get('Education', 0)

        if self.EducationProgram:
            total += percent.get('EducationProgram', 0)

        if self.EducationBoard:
            total += percent.get('EducationBoard', 0)  

        if self.NameOfInstitute:
            total += percent.get('NameOfInstitute', 0)  

        if self.EducationBoard:
            total += percent.get('EducationBoard', 0)  

        if self.MySkill:
            total += percent.get('MySkill', 0)  

        if self.WorkingExperience:
            total += percent.get('WorkingExperience', 0)  

        if self.WorkedField:
            total += percent.get('WorkedField', 0)  

        if self.WorkedCompanyName:
            total += percent.get('WorkedCompanyName', 0)

        if self.WorkedCompanyWebsite:
            total += percent.get('WorkedCompanyWebsite', 0)

        if self.JobCategory:
            total += percent.get('JobCategory', 0)

        if self.Language:
            total += percent.get('Language', 0)

        if self.AboutMe:
            total += percent.get('AboutMe', 0) 

        if self.Facebook:
            total += percent.get('Facebook', 0) 

        if self.Twitter:
            total += percent.get('Twitter', 0) 

        if self.Instagram:
            total += percent.get('Instagram', 0)  

        if self.UploadCv:
            total += percent.get('UploadCv', 0)   
        return total

        






class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name='employerrprofile')
    
    # Basic Information
    CompanyName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Company Name')
    CompanyLogo = models.ImageField(default='defaultlogo.jpg', blank=True, upload_to='Employer/Company_Logos', verbose_name='Company Logo', validators=[Validate_image_extension])
    CompanyCategory = models.CharField(max_length=50, blank=True, choices=JOB_CATEGORY_CHOICES, verbose_name='Company Category')
    CompanyOwnership = models.CharField(max_length=30, blank=True, choices=COMPANY_OWNERSHIP_CHOICES, verbose_name='Company Ownership')
    CompanyWebsite = models.URLField(max_length=100, blank=True, verbose_name='Company Website')
    CompanyEstablishDate = models.DateField(null=True, blank=True, verbose_name='Company Established Date')
    AboutCompany = RichTextField(null=True, blank=True, verbose_name='About Company')

    # Contact Detail
    CompanyAddress = models.CharField(max_length=100, blank=True, verbose_name='Company Address')
    TelNo = models.CharField(max_length=15, blank=True, verbose_name='TelePhone Number')
    MobileNo = models.CharField(max_length=15, blank=True, verbose_name='Mobile Number')

    # Company Social Account
    Facebook = models.URLField(max_length=100, blank=True,)
    Twitter = models.URLField(max_length=100, blank=True,)
    Instagram = models.URLField(max_length=100, blank=True,)

    # Company Person
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    PhoneNumber = models.CharField(max_length=20, blank=False, verbose_name='Phone Number')
    Email = models.EmailField(max_length=30, null=False, blank=True,)


    def __str__(self):
        return f'{self.user.username} profile'


    def get_absolute_url(self):
        return reverse("employer:employer_profile_detail")
    



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        logo = Image.open(self.CompanyLogo.path)
        if logo.height>60 or logo.width>60:
            output_size = (60, 60)
            logo.thumbnail(output_size)
            logo.save(self.CompanyLogo.path)


            
    @property 
    def Company_percentage_complete(self):
        percent = { 'CompanyName': 5, 'CompanyLogo': 5,
                     'CompanyCategory': 6, 'CompanyOwnership':6,
                     'CompanyWebsite':8, 'CompanyEstablishDate':5,
                     'AboutCompany':13, 'CompanyAddress':5,
                     'TelNo':5, 'MobileNo':7,
                     'FirstName':5, 'LastName':5,
                     'PhoneNumber':5, 'Email':5,
                     'Facebook':5, 'Twitter':5, 'Instagram':5,}
        total = 0
        if self.CompanyName:
            total += percent.get('CompanyName', 0)
        if self.CompanyLogo:
            total += percent.get('CompanyLogo', 0)

        if self.CompanyOwnership:
            total += percent.get('CompanyOwnership', 0)

        if self.CompanyCategory:
            total += percent.get('CompanyCategory', 0)

        if self.CompanyWebsite:
            total += percent.get('CompanyWebsite', 0)

        if self.CompanyEstablishDate:
            total += percent.get('CompanyEstablishDate', 0)

        if self.AboutCompany:
            total += percent.get('AboutCompany', 0)

        if self.CompanyAddress:
            total += percent.get('CompanyAddress', 0)

        if self.TelNo:
            total += percent.get('TelNo', 0)

        if self.MobileNo:
            total += percent.get('MobileNo', 0)

        if self.FirstName:
            total += percent.get('FirstName', 0)

        if self.LastName:
            total += percent.get('LastName', 0)

        if self.PhoneNumber:
            total += percent.get('PhoneNumber', 0)  

        if self.Email:
            total += percent.get('Email', 0)  

        if self.Facebook:
            total += percent.get('Facebook', 0)  

        if self.Twitter:
            total += percent.get('Twitter', 0)  

        if self.Instagram:
            total += percent.get('Instagram', 0)

        return total

        