from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

For_FAQ_Choose=(
    (0, "Draft"),
   (1, "Jobseeker"),
   (2, "Employer")
)


class Faqs(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Question')
    answer = RichTextField(verbose_name='Answer')
    for_who = models.IntegerField(choices=For_FAQ_Choose, verbose_name='Faq For', default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
    