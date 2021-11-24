from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

class Grade(models.Model):
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.grade

class Branch(models.Model):
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.branch

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True,null=True)
    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.doctor_name)
        super(Doctor, self).save(*args, **kwargs)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    doctor_name = models.ForeignKey(Doctor,related_name='doc', on_delete=models.CASCADE, null=True,blank=True)
    doctor_username = models.CharField(max_length=100 ,unique=False)
    department = models.ForeignKey(Department,related_name='depart', on_delete=models.CASCADE,null=True,blank=True)
    grade = models.ForeignKey(Grade,related_name='gra', on_delete=models.CASCADE, null=True,blank=True)
    branch = models.ForeignKey(Branch,related_name='bra', on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self):
        return self.subject_name

class Lecture(models.Model):
    lecture_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=False)
    subject_name = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='media/', null=True, blank=True)
    video = models.CharField(max_length=1000, null=True, blank=True)
    assignment_content = models.TextField(max_length=1000 , null=True)
    assignment_end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.lecture_name
    
class Assignment(models.Model):
    assign = models.ForeignKey(Lecture, related_name='assign', on_delete=models.CASCADE)
    solution = models.FileField(upload_to='assignments/', null=True, blank=True)
    solution_added = models.DateField(auto_now=True, auto_now_add=False, null=True, blank=True)

