from django.db import models


class Employee(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=30)
    Salary = models.IntegerField()

    class Meta:
        db_table = 'Employee'