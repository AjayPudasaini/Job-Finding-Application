from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from PIL import Image



GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICE = (
    (GENDER_MALE, 'male'),
    (GENDER_FEMALE, 'female'),
)


MARRIED_STATUS_SINGLE = 'single'
MARRIED_STATUS_MARRIED = 'married'
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
    ('AR', 'Architecture/Interior Designing'),
    ('CE', 'Construction/Engineering'),
    ('CL', 'Commercial/Logistics'),
    ('CGD', 'Creative/Graphic/Designing'),
    ('HP', 'Hospilaty'),
    ('NGO', 'NGO/INGO/Social Work'),
    ('TE', 'Techng/Education'),
    ('GM', 'General MGMT./Administration/Operations'),
    ('HPBM', 'Healthcare/Pharma/Biotech/Medical'),
    ('HRD', 'Human Resources/ Org.Development'),
    ('SP', 'Sales/Public Relations'),
    ('RD', 'Research and Development'),
    ('PMQ', 'Production/Maintenance/Quality'),
    ('MAC', 'Marketing/Advertisement/Custom service'),
    ('LS', 'Legal Services'),
    ('AF', 'Accounting/Finance'),
    ('BIF', 'Banking/Insurance/Finance Services'),
    ('FT', 'Fashion/Textile Designing'),
    ('SFD', 'Secretarial/Front Office/Data Entry'),
    ('IT', 'IT & Telecommunication'),
    ('PS', 'Productive/Securaty Service'),
    ('JE', 'Journalism/Editor/Media'),
    ('O', 'Others'),
)


RELIGION_CHOOSE = (
    ('HI', 'Hinduism'),
    ('BU', 'Buddhism'),
    ('CH', 'Christianity'),
    ('IS', 'Islam'),
    ('SI', 'Sikhism'),
    ('JA', 'Jainism'),
    ('O', 'Others'),
)

NATIONALITY_CHOOSE = (
    ('NP', 'Nepali'),
    ('IN', 'Indian'),
    ('CH', 'Chineases'),
    ('O', 'Others'),
)

EDUCATION_BOARD_CHOICES = (
    ('NB', 'NEB'),
    ('TU', 'Tribhuvan Univercity'),
    ('MWU', 'Mid-Westran Univercity'),
    ('AFU', 'Architure and Forestry Univercity'),
    ('NOU', 'Nepal Open Univercity'),
    ('PU', 'Pokhara Univercity'),
    ('NSU', 'Nepal Sanskrit Univercity'),
    ('NBU', 'Lumbini Buddhist Univercity'),
    ('FWU', 'Far-Western Univercity'),
    ('KU', 'Kathmandu Univercity'),
    ('PU', 'Purbanchal Univercity'),
    ('O', 'Others'), 
)


LANGUAGES_CHOICES = (
    ('NP', 'Nepali'),
    ('EN', 'English'),
    ('O', 'Others'),  
)

COMPANY_OWNERSHIP_CHOICES = (
    ('PU', 'Public'),
    ('PV', 'Private'),
    ('GOV', 'Government'),
    ('O', 'Others'),

)





class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    


class Skill(models.Model):
    Name = TaggableManager()


class Category(models.Model):
    Name = models.CharField(max_length=5, choices=JOB_CATEGORY_CHOICES)



class JobseekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    # Basic Information
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    DateOffBorth = models.DateField(verbose_name='Date Of Birth')
    MarrigeStatus = models.CharField(max_length=7, choices=MARRIED_STATUS_CHOICES, verbose_name='Marrige Status')
    Religion = models.CharField(max_length=2, choices=RELIGION_CHOOSE)
    PhoneNumber = models.CharField(max_length=20, verbose_name='Phone Number')
    Email = models.EmailField(max_length=30, null=False, verbose_name='Email Address')
    Nationality = models.CharField(max_length=1)
    CurrentAddress = models.CharField(max_length=100, verbose_name='Current Address')
    PernamentAddress = models.CharField(max_length=100, verbose_name='Pernament Address')
    ProfileImage = models.ImageField(upload_to = 'Jobseeker/Profile_Pictures', verbose_name='Profile Picture')
   
    # Education Information
    Education = models.CharField(max_length=26, choices=EDUCATION_CHOICES, verbose_name='Education')
    EducationProgram = models.CharField(max_length=200, verbose_name='Education Program')
    EducationBoard = models.CharField(max_length=3, choices=EDUCATION_BOARD_CHOICES, verbose_name='Education Board')
    NameOfInstitute = models.CharField(max_length=200, verbose_name='Name Of Institute')

    # skill
    MySkill = models.ManyToManyField(Skill, verbose_name='My Skill')

    # Past jobs
    WorkingExperience = models.IntegerField(default=0, verbose_name='Working Experience') 
    WorkedField = models.CharField(max_length=50, null=True, verbose_name='Worked Related Fields')  
    WorkedCompanyName = models.CharField(max_length=200, verbose_name='Worked Company Name')
    WorkedCompanyWebsite = models.URLField(max_length=200, verbose_name='Worked Company Website')

    # job category
    JobCategory = models.ManyToManyField(Category, verbose_name='Job Category')

    # add language
    Language = models.CharField(max_length=2, choices=LANGUAGES_CHOICES)

    # about Me
    AboutMe = RichTextField(verbose_name='About Me')

    # Social account
    Facebook = models.URLField(max_length=100)
    Twitter = models.URLField(max_length=100)
    Instagram = models.URLField(max_length=100)

    # upload cv
    UploadCv = models.FileField(upload_to='Jobseeker/CVs', verbose_name='Upload Your CV')





    def __str__(self):
        return f'{self.user.username} profile'

    # def save(self):
    #     super().save()

    #     ProfilePic = Image.open(self.ProfileImage.path)
    #     if ProfilePic.height>100 or ProfilePic.width>100:
    #         output_size = (100, 100)
    #         ProfilePic.thumbnail(output_size)
    #         ProfilePic.save(self.ProfileImage.path)





class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    
    # Basic Information
    CompanyName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Company Name')
    CompanyLogo = models.ImageField(upload_to='Employer/Company_Logos', verbose_name='Company Logo')
    CompanyCategory = models.ManyToManyField(Category, verbose_name='Company Category')
    CompanyOwnership = models.CharField(max_length=3, choices=COMPANY_OWNERSHIP_CHOICES, verbose_name='Company Ownership')
    CompanyWebsite = models.URLField(max_length=100, verbose_name='Company Website')
    CompanyEstablishDate = models.DateField(verbose_name='Company Established Date')
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



    # def save(self):
    #     super().save()

    #     logo = Image.open(self.image.path)
    #     if logo.height>60 or logo.width>60:
    #         output_size = (60, 60)
    #         logo.thumbnail(output_size)
    #         logo.save(self.image.path)



