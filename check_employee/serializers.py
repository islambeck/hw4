from datetime import date

from rest_framework import  serializers
from rest_framework.exceptions import ValidationError

from.models import Department, Positions, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = 'fullname', 'position'


    def birth_date(self,value):
        if date.today().year - value.year <25:
            raise ValidationError("возраст долно быть больше 25")
        return value