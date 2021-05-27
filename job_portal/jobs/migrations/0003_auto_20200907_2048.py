# Generated by Django 3.0.9 on 2020-09-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobpost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Approved', 'Approve'), ('Rejected', 'Reject')], default=0, max_length=20, null=True),
        ),
    ]
