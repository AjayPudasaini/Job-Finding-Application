from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from account.models import JOB_CATEGORY_CHOICES, EDUCATION_CHOICES
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from account.models import User
from PIL import Image







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


Job_SATUS_CHOOSE = (
    ('Pending', 'pending'),
    ('Approved', 'Approve'), 
    ('Rejected', 'Reject'),
)


class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    JobTitle = models.CharField(max_length=500, null=False, blank=False, verbose_name='Job Title')
    Location = models.CharField(max_length=200, choices=LOCATION_CHOOSE, null=False)
    NumberOfVacancies = models.IntegerField(default=0, null=True, verbose_name='Number Of Vancies')
    SalaryStart = models.FloatField(default=0.00, null=True, blank=True, verbose_name='Salary Start With')
    EndSalary = models.FloatField(default=0.00, null=True, blank=True, verbose_name='Salary End With')
    JobLevel = models.CharField(max_length=200, choices=Job_Level_Choices, null=True, verbose_name='Job Level')
    AvaliableTime = models.CharField(max_length=200, choices=JOB_AVALIABLE_TIME, null=True, verbose_name='Avaliable Time')
    JobShift = models.CharField(max_length=100, blank=False, choices=WORKING_SHIFTS, null=True, verbose_name='Job Shift')
    RequiredEducation = models.CharField(max_length=200, blank=False, choices=EDUCATION_CHOICES, null=True, verbose_name='Required Educations')
    RequiredExperience = models.IntegerField(default=0, blank=False, null=True, verbose_name='Required Experience')
    RequiredSkill = models.CharField(max_length=250, verbose_name='Required Skills', blank=False, null=True)
    JobCategory = models.CharField(max_length=200, choices=JOB_CATEGORY_CHOICES, null=False, blank=False, verbose_name='Job Category')
    Gender = models.CharField(max_length=50, blank=False, choices=Gender, default='Both', null=True, verbose_name='Required Gender')
    JobDescreptions = RichTextField(verbose_name='Job Descriptions', blank=False, null=False)
    JobSpecification = RichTextField(verbose_name='Job Specification', blank=False, null=True)
    ApplyLink = models.URLField(max_length=500, verbose_name='Job Apply Link', blank=True, null=True)
    HiringBanner = models.ImageField(default='DefaultHireBanner.jpg', upload_to='Employer/Hire Banners', null=True , blank=False, verbose_name='Hiring Banner')
    SaveJob = models.ManyToManyField(User, related_name='savejob', blank=True)
    status = models.CharField(max_length=20, choices=Job_SATUS_CHOOSE, null=True, default='Pending')


    views = models.IntegerField(default=0)


    JobPostDate = models.DateTimeField(default=timezone.now, blank=False)
    JobExpiryDate = models.DateTimeField()


    def __str__(self):
        return self.JobTitle
    

    def get_absolute_url(self):
        return reverse("employer:employer_dashboard", kwargs={'username':self.user.username})

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        HireBanner = Image.open(self.HiringBanner.path)
        if HireBanner.height>400 or HireBanner.width>760:
            output_size = (400, 760)
            HireBanner.thumbnail(output_size)
            HireBanner.save(self.HiringBanner.path)




class JobApply(models.Model):
    user = models.ForeignKey(User, related_name='applyersname', on_delete = models.CASCADE)
    job = models.ForeignKey(JobPost, related_name='jobapplys', on_delete = models.CASCADE, verbose_name='Apply Job')
    JobApplyReason = RichTextField(verbose_name='Why apply this job')
    ApplydDate = models.DateTimeField(default=timezone.now, verbose_name='Job Apply Date')


    def get_absolute_url(self):
        return reverse("browse_job")

    def __str__(self):
        return f'{self.user.username + self.job.JobTitle} applied'
    

    class Meta():
        ordering = ['-ApplydDate']
    
    



   
    


