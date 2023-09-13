from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics

from.models import Department,Positions,Employee
from .serializers import DepartmentSerializer,PositionsSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionsViewSet(ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentEmployeesAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        return Employee.objects.filter(department_id=department_id)
