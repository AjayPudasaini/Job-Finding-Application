from django.contrib import admin
from account.models import User,  EmployerProfile, JobseekerProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_employer', 'is_jobseeker', 'is_superuser' ]

@admin.register(JobseekerProfile)
class JobseekerProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user','FirstName']



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
    