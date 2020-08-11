from django.db.models.signals import post_save
from account.models import JobseekerProfile
from django.contrib.auth.models import User
from django.dispatch  import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **Kwargs):
    if created:
        JobseekerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **Kwargs):
    instance.jobseekerprofile.save()