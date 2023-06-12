# Generated by Django 4.2.1 on 2023-06-12 09:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_cv_job_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='cv_file',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='CV_file'),
        ),
    ]
