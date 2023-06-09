# Generated by Django 4.2.1 on 2023-06-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('job', '0007_category_slug_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Applicant',
            field=models.ManyToManyField(related_name='applicant_job', to='users.employer'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.TextField(),
        ),
    ]
