from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Profile
from subjects.models import Subject
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'
    fields ='__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('accounts:subjects')
    
def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'accounts/profile/profile.html',{'profile':profile})


def subjects(request):
    profile = Profile.objects.get(user = request.user)
    if request.user.is_superuser:
        subjects = Subject.objects.all()
    elif request.user.is_staff:
        subjects = Subject.objects.filter(doctor_username=request.user.username)
    elif request.user.is_authenticated:
        subjects = Subject.objects.filter(grade=profile.grade , department=profile.department,branch=profile.branch)
    return render(request,'accounts/subject_list.html', {'subjects':subjects,'profile':profile})

def profile_list(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile-settings.html' , {'profile':profile})
class ProfileEdit(UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    fields =['image','phone_number','address']
    success_url = reverse_lazy('accounts:subjects')

def last_profile(request):
    last_profile = Profile.objects.last()
    return render(request,'accounts/last_profile_settings.html' , {'last_profile':last_profile})
class LastProfileEdit(UpdateView):
    model = Profile
    template_name = 'accounts/edit_last_profile.html'
    fields =['image','national_id','address','department','grade','branch']
    success_url = reverse_lazy('settings:user-settings')