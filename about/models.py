from django.db import models
from django.utils.text import slugify

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=150)
    faculty_name_link = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image =  models.ImageField(upload_to='faculty_images/', null=True)
    place = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/')
    logo_link = models.CharField(max_length=200)
    face_book_link = models.CharField(max_length=200)
    tweeter_link = models.CharField(max_length=200)
    google_link = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)
    main_email = models.CharField(max_length=200)
    main_phone = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.faculty_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.faculty_name)
        super(Faculty, self).save(*args, **kwargs)
