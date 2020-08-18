from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager
from account.models import JOB_CATEGORY_CHOICES, EDUCATION_CHOICES
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator




LOCATION_CHOOSE = (
    ('Kathmandu', 'Kathmandu'),
    ('Bhaktaput', 'Bhaktaput'),
    ('Lalitpur', 'Lalitpur'),
    ('Dhading', 'Dhading'),
    ('Nuwakot', 'Nuwakot'),
    ('Kavre', 'Kavre'),
    ('Pokhara', 'Pokhara'),
    ('Mahottari', 'Mahottari'),
    ('Achham', 'Achham'),
    ('Baglung', 'Baglung'),
    ('Baghang', 'Baghang'),
    ('Bajura', 'Bajura'),
    ('Bake', 'Bake'),
    ('Bara', 'Bara'),
    ('Surkhet', 'Surkhet'),
    ('Dhangadhi', 'Dhangadhi'),
    ('Biratnagar', 'Biratnagar'),
    ('Nepaljung', 'Nepaljung'),
    ('Parsha', 'Parsha'),
    ('Palpa', 'Palpa'),
    ('Ilam', 'Ilam'),
    ('Jhapa', 'JJhapa'),
    ('RajBiraj', 'RajBiraj'),
    ('Janakpur', 'Janakpur'),
    ('Rashuwa', 'Rashwa'),
    ('Gorkha', 'Gorkha'),
    ('Manang/Mustang', 'Manang/Mustang'),
    ('Humla', 'Humla'),
    ('Jumla', 'Jumla'),
    ('Karnali', 'Karnali'),
    ('Mugu', 'Mugu'),
    
)

Job_Level_Choices = (
    ('Internship Level', 'Internship Level'),
    ('Entry Lavel', 'Entry Level'),
    ('Intermidate Lavel', 'Intermidate Lavel'),
    ('Expert Level', 'Expert Level'),
    ('Internship/Entry Level', 'Internship/Entry Level'),
    ('Entry/Intermidate Lavel', 'Entry/Intermidate Level'),
    ('Intermidate/Expert Lavel', 'Intermidate/Expert Lavel'),
    ('Expert/Entry Level', 'Expert/Entry Level')
)


JOB_AVALIABLE_TIME = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Work From Home', 'Work From Home'),
    ('Part/Full Time', 'Part/Full Time'),
    ('Full/Work From Home Time', 'Full/Work From Home Time'),
    ('Work From Home/Part Time', 'Work From Home/Part Time'),
    ('Work From Home/Full Time', 'Work From Home/Full Time'),
    
)

WORKING_SHIFTS = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
    ('Morning/Day', 'Morning/Day'),
    ('Evening/Night', 'Evening/Night'),   
)


Gender = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Both', 'Both'),   
)




class JobPost(models.Model):
    job_post_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    JobTitle = models.CharField(max_length=500, null=False, blank=False, verbose_name='Job Title')
    Location = models.CharField(max_length=200, choices=LOCATION_CHOOSE, null=False)
    NumberOfVacancies = models.IntegerField(default=0, null=True, verbose_name='Number Of Vancies')
    SalaryStart = models.FloatField(default=0.00, null=True, verbose_name='Salary Start With')
    EndSalary = models.FloatField(default=0.00, null=True, verbose_name='Salary End With')
    JobLevel = models.CharField(max_length=200, choices=Job_Level_Choices, null=True, verbose_name='Job Level')
    AvaliableTime = models.CharField(max_length=200, choices=JOB_AVALIABLE_TIME, null=True, verbose_name='Avaliable Time')
    JobShift = models.CharField(max_length=100, choices=WORKING_SHIFTS, null=True, verbose_name='Job Shift')
    RequiredEducation = models.CharField(max_length=200, choices=EDUCATION_CHOICES, null=True, verbose_name='Required Educations')
    RequiredExperience = models.IntegerField(default=0, null=True, verbose_name='Required Experience')
    RequiredSkill = TaggableManager(verbose_name='Required Skills')
    JobCategory = models.CharField(max_length=200, choices=JOB_CATEGORY_CHOICES, null=False, verbose_name='Job Category')
    Gender = models.CharField(max_length=50, choices=Gender, default='Both', null=True)
    JobDescreptions = RichTextField(verbose_name='Job Descriptions', null=False)
    HiringBanner = models.ImageField(default='DefaultHireBanner.jpg', upload_to='Employer/Hire Banners', null=True , verbose_name='Hiring Banner')


    JobPostDate = models.DateTimeField(default=timezone.now)
    JobExpiryDate = models.DateTimeField()

