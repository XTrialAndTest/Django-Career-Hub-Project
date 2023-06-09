# Generated by Django 4.2.1 on 2023-06-09 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_applicant_cv_job_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='cv',
        ),
        migrations.AddField(
            model_name='job',
            name='cv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant_CV', to='job.applicant_cv'),
        ),
    ]
