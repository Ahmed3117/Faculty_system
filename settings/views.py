from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from subjects.models import Doctor, Subject, Assignment, Branch, Department, Grade
from about.models import Faculty
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

def settings(request):
    settings = ['faculty-settings','user-settings','subject-settings','doctor-settings','department-settings','grade-settings','branch-settings'] 
    return render(request,'settings/settings.html',{'settings':settings})
class FacultyList(ListView):
    model = Faculty
    context_object_name = 'faculties'
    template_name = 'settings/faculty-settings.html'
    
class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'settings/user-settings.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['users'] = context['users'].filter(
                username__icontains=search_input
            )
        context['search_input'] = search_input
        return context

class SubjectList(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'settings/subject-settings.html'

class DoctorList(ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'settings/doctor-settings.html'

class DepartmentList(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'settings/department-settings.html'

class GradeList(ListView):
    model = Grade
    context_object_name = 'grades'
    template_name = 'settings/grade-settings.html'

class BranchList(ListView):
    model = Branch
    context_object_name = 'branchs'
    template_name = 'settings/branch-settings.html'

###############################################################
class UserCreate(CreateView):
    model = User
    template_name = 'settings/Register.html'
    fields =['username','first_name','last_name', 'password','is_staff']
    success_url = reverse_lazy('accounts:last-profile')
    # success_url = reverse_lazy('settings:user-settings')
class FacultyCreate(CreateView):
    model = Faculty
    template_name = 'settings/create_faculty.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:faculty-settings')

class SubjectCreate(CreateView):
    model = Subject
    template_name = 'settings/create_subject.html'
    fields =['subject_name','description','doctor_name', 'department', 'grade', 'branch']
    success_url = reverse_lazy('settings:subject-settings')

class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'settings/create_doctor.html'
    fields =['doctor_name']
    success_url = reverse_lazy('settings:doctor-settings')

class DepartmentCreate(CreateView):
    model = Department
    template_name = 'settings/create_department.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:department-settings')

class GradeCreate(CreateView):
    model = Grade
    template_name = 'settings/create_grade.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:grade-settings')
    
class BranchCreate(CreateView):
    model = Branch
    template_name = 'settings/create_branch.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:branch-settings')
    
################################
class FacultyEdit(UpdateView):
    model = Faculty
    template_name = 'settings/edit_faculty.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:faculty-settings')

class UserEdit(UpdateView):
    model = User
    template_name = 'settings/edit_user.html'
    fields =['username','first_name','last_name', 'password','is_staff']
    success_url = reverse_lazy('settings:user-settings')
class SubjectEdit(UpdateView):
    model = Subject
    template_name = 'settings/edit_subject.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:subject-settings')

class DoctorEdit(UpdateView):
    model = Doctor
    template_name = 'settings/edit_doctor.html'
    fields =['doctor_name']
    success_url = reverse_lazy('settings:doctor-settings')

class DepartmentEdit(UpdateView):
    model = Department
    template_name = 'settings/edit_department.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:department-settings')

class GradeEdit(UpdateView):
    model = Grade
    template_name = 'settings/edit_grade.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:grade-settings')

class BranchEdit(UpdateView):
    model = Branch
    template_name = 'settings/edit_branch.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:branch-settings')

###################################
class FacultyDelete(DeleteView):
    model = Faculty
    context_object_name = 'faculty'
    template_name = 'settings/delete_faculty.html'
    success_url = reverse_lazy('settings:faculty-settings')

class UserDelete(DeleteView):
    model = User
    context_object_name = 'user'
    template_name = 'settings/delete_user.html'
    success_url = reverse_lazy('settings:user-settings')
class SubjectDelete(DeleteView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'settings/delete_subject.html'
    success_url = reverse_lazy('settings:subject-settings')

class DoctorDelete(DeleteView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'settings/delete_doctor.html'
    success_url = reverse_lazy('settings:doctor-settings')

class DepartmentDelete(DeleteView):
    model = Department
    context_object_name = 'department'
    template_name = 'settings/delete_department.html'
    success_url = reverse_lazy('settings:department-settings')

class GradeDelete(DeleteView):
    model = Grade
    context_object_name = 'grade'
    template_name = 'settings/delete_grade.html'
    success_url = reverse_lazy('settings:grade-settings')

class BranchDelete(DeleteView):
    model = Branch
    context_object_name = 'branch'
    template_name = 'settings/delete_branch.html'
    success_url = reverse_lazy('settings:branch-settings')