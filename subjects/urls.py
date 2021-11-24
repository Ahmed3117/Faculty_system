from django.urls import path
from .api_view import SubjectList, SubjectCreate, SubjectRUD, LectureList, LectureCreate, LectureRUD, DepartmentList, DepartmentCreate, DepartmentRUD, GradeList, GradeCreate, GradeRUD, BranchList, BranchCreate, BranchRUD
from .views import SubjectDetail, LectureCreate, LectureEdit, LectureDelete
app_name = 'subjects'
urlpatterns = [
    # api urls
    path("api/subjectlist/", SubjectList.as_view(), name="apisubjectlist"),
    path("api/subjectcreate/", SubjectCreate.as_view(), name="apisubjectcreate"),
    path("api/subjectrud/<int:pk>", SubjectRUD.as_view(), name="apisubjectrud"),
    path("api/lecturelist/", LectureList.as_view(), name="apilecturelist"),
    path("api/lecturecreate/", LectureCreate.as_view(), name="apilecturecreate"),
    path("api/lecturerud/<int:pk>", LectureRUD.as_view(), name="apilecturerud"),
    path("api/departmentlist/", DepartmentList.as_view(), name="apidepartmentlist"),
    path("api/departmentcreate/", DepartmentCreate.as_view(), name="apidepartmentcreate"),
    path("api/departmentrud/<int:pk>", DepartmentRUD.as_view(), name="apidepartmentrud"),
    path("api/gradelist/", GradeList.as_view(), name="apigradelist"),
    path("api/gradecreate/", GradeCreate.as_view(), name="apigradecreate"),
    path("api/graderud/<int:pk>", GradeRUD.as_view(), name="apigraderud"),
    path("api/branchlist/", BranchList.as_view(), name="apibranchlist"),
    path("api/branchcreate/", BranchCreate.as_view(), name="apibranchcreate"),
    path("api/branchrud/<int:pk>", BranchRUD.as_view(), name="apibranchrud"),
    # static urls
    path("lectures/<int:pk>", SubjectDetail.as_view(), name="lectures"),
    path("lecture-create/", LectureCreate.as_view(), name="lecture-create"),
    path('lecture-edit/<int:pk>',LectureEdit.as_view(),name='lecture-edit'),
    path('lecture-delete/<int:pk>',LectureDelete.as_view(),name='lecture-delete'),
]