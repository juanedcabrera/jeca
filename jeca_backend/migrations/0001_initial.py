# Generated by Django 4.2.3 on 2023-07-26 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('considering', 'Considering'), ('applied', 'Applied'), ('network', 'Network'), ('phone_screen', 'Phone Screen'), ('interview_scheduled', 'Interview Scheduled'), ('offer_received', 'Offer Received'), ('rejected', 'Rejected')], default='considering', max_length=20)),
                ('application_date', models.DateField()),
                ('post_date', models.DateField()),
                ('job_description', models.TextField()),
                ('job_url', models.URLField(blank=True, null=True)),
                ('feedback_tracker', models.CharField(max_length=400)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeca_backend.company')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeca_backend.job')),
            ],
        ),
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeca_backend.job')),
            ],
        ),
    ]
