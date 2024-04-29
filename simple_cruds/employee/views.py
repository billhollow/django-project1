from rest_framework import viewsets

from simple_cruds.employee.models import Employee
from simple_cruds.employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

