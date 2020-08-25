# Generated by Django 3.0.9 on 2020-08-23 14:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0006_auto_20200822_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobApplyReason', ckeditor.fields.RichTextField()),
                ('ApplydDate', models.DateField(default=django.utils.timezone.now, verbose_name='Job Apply Date')),
                ('jobpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobPost', verbose_name='Apply Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
