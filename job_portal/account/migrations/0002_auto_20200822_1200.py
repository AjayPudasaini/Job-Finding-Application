# Generated by Django 3.0.9 on 2020-08-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='MySkill',
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='MySkill',
            field=models.CharField(max_length=250, null=True, verbose_name='My Skill'),
        ),
    ]
