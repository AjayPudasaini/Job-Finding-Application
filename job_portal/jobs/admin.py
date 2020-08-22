from django.contrib import admin
from jobs.models import JobPost

# Register your models here.
# admin.site.register(JobPost)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['JobTitle', 'user']



