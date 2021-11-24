from rest_framework.serializers import ModelSerializer
from .models import Subject, Lecture,Department, Branch, Grade, Assignment

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'