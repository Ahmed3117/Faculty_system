from django.http import response
from django.shortcuts import render
from .models import Faculty
from .serializers import FacultySerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# About
# any user can see about
class FacultyList(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#only admin can create about
class FacultyCreate(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
#only admin can retrieve , update and delete about

class FacultyRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


