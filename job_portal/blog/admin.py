from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status']