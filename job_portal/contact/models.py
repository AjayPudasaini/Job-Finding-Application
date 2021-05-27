from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Contact(models.Model):
    FullName = models.CharField(max_length=50, verbose_name='Full Name')
    Email = models.EmailField(max_length=256, verbose_name='Email Address')
    Queries = RichTextField(verbose_name='Questions/Messages')
    CreateDate = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.FullName} Queries'
    