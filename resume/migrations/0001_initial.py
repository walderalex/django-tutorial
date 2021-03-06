# Generated by Django 2.2.15 on 2020-08-30 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('personal_summary', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=12)),
                ('display_name', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role_or_title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('job_description', models.TextField()),
                ('job_start_date', models.DateField()),
                ('job_end_date', models.DateField()),
                ('resume', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_or_hobby', models.TextField()),
                ('resume', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('school_start_date', models.DateField()),
                ('school_end_date', models.DateField()),
                ('best_subject', models.CharField(max_length=200)),
                ('resume', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
    ]
