from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from PIL import Image
from django.urls import reverse





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
    Gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    MarrigeStatus = models.CharField(max_length=20, choices=MARRIED_STATUS_CHOICES, verbose_name='Marrige Status')
    Religion = models.CharField(max_length=20, choices=RELIGION_CHOOSE)
    PhoneNumber = models.CharField(max_length=20, verbose_name='Phone Number')
    Nationality = models.CharField(max_length=30, choices=NATIONALITY_CHOOSE, verbose_name='Nationality')
    CurrentAddress = models.CharField(max_length=100, verbose_name='Current Address')
    PernamentAddress = models.CharField(max_length=100, verbose_name='Pernament Address')
    ProfileImage = models.ImageField(default='defaultusers.png', upload_to = 'Jobseeker/Profile_Pictures', verbose_name='Profile Picture')
   
    # Education Information
    Education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, verbose_name='Education')
    EducationProgram = models.CharField(max_length=200, verbose_name='Education Program')
    EducationBoard = models.CharField(max_length=100, choices=EDUCATION_BOARD_CHOICES, verbose_name='Education Board')
    NameOfInstitute = models.CharField(max_length=200, verbose_name='Name Of Institute')

    # skill
    MySkill = models.CharField(max_length=250, verbose_name='My Skill', null=True)

    # Past jobs
    WorkingExperience = models.IntegerField(default=0, verbose_name='Working Experience') 
    WorkedField = models.CharField(max_length=50, null=True, verbose_name='Worked Related Fields')  
    WorkedCompanyName = models.CharField(max_length=200, verbose_name='Worked Company Name')
    WorkedCompanyWebsite = models.URLField(max_length=200, verbose_name='Worked Company Website')

    # job category
    JobCategory = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES, verbose_name='Job Category')

    # add language
    Language = models.CharField(max_length=20, choices=LANGUAGES_CHOICES)

    # about Me
    AboutMe = RichTextField(verbose_name='About Me')

    # Social account
    Facebook = models.URLField(max_length=100)
    Twitter = models.URLField(max_length=100)
    Instagram = models.URLField(max_length=100)

    # upload cv
    UploadCv = models.FileField(upload_to='Jobseeker/CVs',null=True,  verbose_name='Upload Your CV')





    def __str__(self):
        return f'{self.user.username} profile'


    # def get_absolute_url(self):
    #     return reverse("jobseeker:jobseeker_profile_detail")



    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ProfilePic = Image.open(self.ProfileImage.path)
        if ProfilePic.height>300 or ProfilePic.width>300:
            output_size = (300, 300)
            ProfilePic.thumbnail(output_size)
            ProfilePic.save(self.ProfileImage.path)





class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name='employerrprofile')
    
    # Basic Information
    CompanyName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Company Name')
    CompanyLogo = models.ImageField(default='defaultlogo.jpg', upload_to='Employer/Company_Logos', verbose_name='Company Logo')
    CompanyCategory = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES, verbose_name='Company Category')
    CompanyOwnership = models.CharField(max_length=30, choices=COMPANY_OWNERSHIP_CHOICES, verbose_name='Company Ownership')
    CompanyWebsite = models.URLField(max_length=100, verbose_name='Company Website')
    CompanyEstablishDate = models.DateField(null=True, blank=True, verbose_name='Company Established Date')
    AboutCompany = RichTextField(null=True, verbose_name='About Company')

    # Contact Detail
    CompanyAddress = models.CharField(max_length=100, verbose_name='Company Address')
    TelNo = models.CharField(max_length=15, verbose_name='TelePhone Number')
    MobileNo = models.CharField(max_length=15, verbose_name='Mobile Number')

    # Company Social Account
    Facebook = models.URLField(max_length=100)
    Twitter = models.URLField(max_length=100)
    Instagram = models.URLField(max_length=100)

    # Company Person
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    PhoneNumber = models.CharField(max_length=20, verbose_name='Phone Number')
    Email = models.EmailField(max_length=30, null=False)


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



