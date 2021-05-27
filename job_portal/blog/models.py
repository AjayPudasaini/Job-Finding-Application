from django.db import models
from account.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_author')
    updated_on = models.DateTimeField(default=timezone.now)
    content = RichTextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
