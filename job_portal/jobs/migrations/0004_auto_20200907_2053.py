# Generated by Django 3.0.9 on 2020-09-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200907_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Approved', 'Approve'), ('Rejected', 'Reject')], default='Pending', max_length=20, null=True),
        ),
    ]
