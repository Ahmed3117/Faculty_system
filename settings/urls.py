from django.urls import path
from .views import UserDelete, UserEdit, settings,UserList, FacultyList,UserCreate, FacultyCreate, DoctorCreate, SubjectCreate,DepartmentCreate, GradeCreate, BranchCreate, SubjectList, DepartmentList, DoctorList, GradeList, BranchList, BranchEdit,BranchDelete,FacultyEdit,SubjectEdit,DoctorEdit,DepartmentEdit,GradeEdit,FacultyDelete,SubjectDelete,DoctorDelete,DepartmentDelete,GradeDelete
app_name = 'settings'

urlpatterns = [
    path("settings", settings, name="settings"),
    path("faculty-settings", FacultyList.as_view(), name="faculty-settings"),
    path("user-settings", UserList.as_view(), name="user-settings"),
    path("subject-settings", SubjectList.as_view(), name="subject-settings"),
    path("doctor-settings", DoctorList.as_view(), name="doctor-settings"),
    path("department-settings", DepartmentList.as_view(), name="department-settings"),
    path("grade-settings", GradeList.as_view(), name="grade-settings"),
    path("branch-settings", BranchList.as_view(), name="branch-settings"),
    #####################################
    path("user-create", UserCreate.as_view(), name="user-create"),
    path("faculty-create", FacultyCreate.as_view(), name="faculty-create"),
    path("subject-create", SubjectCreate.as_view(), name="subject-create"),
    path('doctor-create',DoctorCreate.as_view(),name='doctor-create'),
    path('department-create',DepartmentCreate.as_view(),name='department-create'),
    path('grade-create',GradeCreate.as_view(),name='grade-create'),
    path('branch-create',BranchCreate.as_view(),name='branch-create'),
    ########################################
    path('faculty-edit/<int:pk>',FacultyEdit.as_view(),name='faculty-edit'),
    path('user-edit/<int:pk>',UserEdit.as_view(),name='user-edit'),
    path('subject-edit/<int:pk>',SubjectEdit.as_view(),name='subject-edit'),
    path('doctor-edit/<int:pk>',DoctorEdit.as_view(),name='doctor-edit'),
    path('department-edit/<int:pk>',DepartmentEdit.as_view(),name='department-edit'),
    path('grade-edit/<int:pk>',GradeEdit.as_view(),name='grade-edit'),
    path('branch-edit/<int:pk>',BranchEdit.as_view(),name='branch-edit'),
    #########################################
    path('faculty-delete/<int:pk>',FacultyDelete.as_view(),name='faculty-delete'),
    path('user-delete/<int:pk>',UserDelete.as_view(),name='user-delete'),
    path('subject-delete/<int:pk>',SubjectDelete.as_view(),name='subject-delete'),
    path('doctor-delete/<int:pk>',DoctorDelete.as_view(),name='doctor-delete'),
    path('department-delete/<int:pk>',DepartmentDelete.as_view(),name='department-delete'),
    path('grade-delete/<int:pk>',GradeDelete.as_view(),name='grade-delete'),
    path('branch-delete/<int:pk>',BranchDelete.as_view(),name='branch-delete'),
]
