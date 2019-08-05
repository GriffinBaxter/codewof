# Generated by Django 2.1.5 on 2019-08-04 23:29

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codewof', '0003_questiontypedebugging_initial_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('visible', models.BooleanField(default=False, help_text='Set to true when study should be listed to users.')),
                ('consent_form', models.CharField(help_text='Name of class for consent form.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of group, hidden from users and source control.', max_length=200)),
                ('questions', models.ManyToManyField(blank=True, related_name='study_groups', to='codewof.Question')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_groups', to='research.Study')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudyRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('send_study_results', models.BooleanField(default=False)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_registrations', to='research.Study')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
