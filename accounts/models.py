from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from subjects.models import Department, Grade, Branch
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/' , blank=True, null=True)
    national_id = models.CharField(max_length=14 ,unique=False)
    phone_number = models.CharField(max_length=11 , blank=True, null=True)
    address = models.CharField(max_length=100 , blank=True, null=True)
    department = models.ForeignKey(Department,related_name='d', on_delete=models.CASCADE,null=True,blank=True)
    grade = models.ForeignKey(Grade,related_name='g', on_delete=models.CASCADE, null=True,blank=True)
    branch = models.ForeignKey(Branch,related_name='b', on_delete=models.CASCADE, null=True,blank=True)
    
    
    def __str__(self):
        return str(self.user)
    
    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)
