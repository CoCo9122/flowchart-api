from rest_framework import serializers
from .models import Employee, EmployeeChart

class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeChartSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeChart
        fields = '__all__'