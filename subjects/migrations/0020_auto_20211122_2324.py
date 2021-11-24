# Generated by Django 3.2.9 on 2021-11-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0019_subject_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='slug',
        ),
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]