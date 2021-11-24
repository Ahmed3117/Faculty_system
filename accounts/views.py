from django.shortcuts import render
from .models import Profile
from subjects.models import Subject, Doctor
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
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
    return render(request,'accounts/subject_list.html' , {'subjects':subjects,'profile':profile})
