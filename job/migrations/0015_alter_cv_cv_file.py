# Generated by Django 4.2.1 on 2023-06-13 15:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_remove_cv_cv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv_file',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='CV(PNG/JPEG)'),
        ),
    ]
