# Generated by Django 4.2.1 on 2023-06-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_alter_job_applicant_job_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_application',
            name='job',
        ),
    ]
