# Generated by Django 3.2.9 on 2021-11-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=150)),
                ('faculty_name_link', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='faculty_images/')),
                ('place', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('logo_link', models.CharField(max_length=200)),
                ('face_book_link', models.CharField(max_length=200)),
                ('tweeter_link', models.CharField(max_length=200)),
                ('google_link', models.CharField(max_length=200)),
                ('youtube_link', models.CharField(max_length=200)),
                ('insta_link', models.CharField(max_length=200)),
                ('main_email', models.CharField(max_length=200)),
                ('main_phone', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]