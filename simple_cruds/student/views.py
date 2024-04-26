from rest_framework import viewsets
from simple_cruds.student.models import Student
from simple_cruds.student.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

