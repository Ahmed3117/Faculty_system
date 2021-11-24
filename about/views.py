from django.shortcuts import render
from .models import Faculty

def faculty_information(request):
    faculty_info= Faculty.objects.last()
    return render(request,'about/home.html',{'faculty_info':faculty_info})
