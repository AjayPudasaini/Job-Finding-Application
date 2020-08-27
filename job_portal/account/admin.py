from django.contrib import admin
from account.models import User,  EmployerProfile, JobseekerProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_employer', 'is_jobseeker', 'is_superuser' ]

@admin.register(JobseekerProfile)
class JobseekerProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User', {
            "fields": (
                'user', 'FirstName', 'LastName'
            ),
        }),

        ('Basic Personal Information', {
            "fields": (
                'MarrigeStatus','Gender','Religion','PhoneNumber','Nationality','CurrentAddress', 'PernamentAddress', 'ProfileImage'
            ),
        }),

        ('Education Information', {
            "fields": (
                'Education','EducationProgram','EducationBoard', 'NameOfInstitute',
            ),
        }),
        ('Skill', {
            "fields": (
                'MySkill',
            ),
        }),

        ('Past Jobs', {
            "fields": (
                'WorkingExperience','WorkedField','WorkedCompanyName', 'WorkedCompanyWebsite'
            ),
        }),

        ('Job Category', {
            "fields": (
                'JobCategory',
            ),
        }),

        ('Language', {
            "fields": (
                'Language',
            ),
        }),

        ('About', {
            "fields": (
                'AboutMe',
            ),
        }),

        ('Personal Social Account', {
            "fields": (
                'Facebook','Twitter','Instagram'
            ),
        }),

        ('Cvs', {
            "fields": (
                'UploadCv',
            ),
        }),


        
    )
    



@admin.register(EmployerProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User', {
            "fields": (
                'user', 'CompanyName'
            ),
        }),
        ('Company Basic Information', {
            "fields": (
                'CompanyLogo','CompanyCategory','CompanyOwnership','CompanyWebsite','CompanyEstablishDate','AboutCompany'
            ),
        }),

        ('Company Contact Detail', {
            "fields": (
                'CompanyAddress','TelNo','MobileNo'
            ),
        }),

        ('Company Social Account', {
            "fields": (
                'Facebook','Twitter','Instagram'
            ),
        }),

        ("Company Person's personal Detail", {
            "fields": (
                'FirstName','LastName','PhoneNumber','Email'
            ),
        }),
    )
    