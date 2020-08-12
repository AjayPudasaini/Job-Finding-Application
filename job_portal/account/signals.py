from django.db.models.signals import post_save
from account.models import JobseekerProfile, EmployerProfile
from django.contrib.auth.models import User
from django.dispatch  import receiver

@receiver(post_save, sender=User)
def create_jobseeker_profile(sender, instance, created, **Kwargs):
    if created:
        JobseekerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_jobseeker_profile(sender, instance, **Kwargs):
    instance.jobseekerprofile.save()



@receiver(post_save, sender=User)
def create_employer_profile(sender, instance, created, **Kwargs):
    if created:
        EmployerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_employer_profile(sender, instance, **Kwargs):
    instance.employerprofile.save()