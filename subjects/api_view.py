# from django.http import response
from django.shortcuts import render
from .models import Subject, Lecture, Department, Grade, Branch, Assignment
from .serializers import SubjectSerializer, LectureSerializer, DepartmentSerializer, GradeSerializer, BranchSerializer, AssignmentSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework.decorators import api_view,authentication_classes,permission_classes
# from rest_framework.response import Response
# from rest_framework import status


# Subject
# any user can see Subject
###### modify######### if user is student he see all subjects but if user is doctor he hust see his subjects (user.username=doctorname)
class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#only admin can create Subject
class SubjectCreate(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
#only admin can retrieve , update and delete Subject

class SubjectRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

# lectures
# any user can list lectures
###### modify######### if user is student he see all lectures but if user is doctor he hust see his lectures 
class LectureList(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

###### modify######### only doctor can create a lecture
class LectureCreate(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
###### modify######### only doctor can rud a lecture
class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# Department
# any user can see Department
class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#only admin can create Department
class DepartmentCreate(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
#only admin can retrieve , update and delete Department
class DepartmentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

# Grade
# any user can see Grade
class GradeList(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#only admin can create Grade
class GradeCreate(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
#only admin can retrieve , update and delete Grade
class GradeRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


# Branch
# any user can see Branch
class BranchList(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#only admin can create Grade
class BranchCreate(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
#only admin can retrieve , update and delete Grade
class BranchRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
#! we didn't make apis for Assignment  