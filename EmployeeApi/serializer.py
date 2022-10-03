from rest_framework import serializers
from EmployeeApi import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('Id','Name','Department','Salary')
        
