# Generated by Django 4.2.1 on 2023-06-06 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Web developer', 'Web developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Frontend developer', 'Frontend developer'), ('Backend developer', 'Backend developer'), ('Database admin', 'Database admin'), ('Data analyst', 'Data analyst')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_location', models.CharField(max_length=200)),
                ('contract_type', models.CharField(choices=[('remote', 'remote'), ('part-time', 'part-time'), ('full-time', 'full-time'), ('negotiations', 'negotiations')], max_length=200)),
                ('position', models.CharField(choices=[('junior', 'junior'), ('intermediate', 'intermediate'), ('senior', 'senior'), ('expart', 'expart')], max_length=200)),
                ('job_description', models.TextField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='users.employer')),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoties', to='job.categories')),
            ],
        ),
    ]
