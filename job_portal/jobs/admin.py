from django.contrib import admin
from jobs.models import JobPost, JobApply

# Register your models here.
# admin.site.register(JobPost)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'JobTitle', 'user']


@admin.register(JobApply)
class JobApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'job', 'job_id', 'user', 'user_id', 'JobApplyReason']



