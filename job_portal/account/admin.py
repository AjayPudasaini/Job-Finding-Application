from django.contrib import admin
from account.models import User,  EmployerProfile, JobseekerProfile, Skill, Category


admin.site.register(User)
# admin.site.register(EmployerProfile)
admin.site.register(JobseekerProfile)
# admin.site.register(Skill)
# admin.site.register(Category)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'is_employer', 'is_jobseeker', 'is_superuser' ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','Name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','Name']

    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('Name')

    # def tag_list(self, obj):
    #     return u", ".join(o.name for o in obj.Name.all())




@admin.register(EmployerProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Basic Information', {
            "fields": (
                'CompanyName','CompanyLogo','CompanyCategory','CompanyOwnership','CompanyWebsite','CompanyEstablishDate','AboutCompany'
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
    