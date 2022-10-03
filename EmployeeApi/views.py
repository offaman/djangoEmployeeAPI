from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApi.models import Employee
from EmployeeApi.serializer import EmployeeSerializer


def Employees(request,id = None):
    if request.method == 'GET':
        AllEmployees = Employee.objects.all()
        serializedEmployees = EmployeeSerializer(AllEmployees,many = True)
        return JsonResponse(serializedEmployees.data,safe=False)
    elif request.method == 'DELETE':
        EmployeeToDelete = Employee.objects.all()
        EmployeeToDelete.delete()
        return JsonResponse("Deleted Successfully",safe = False)

    elif request.method == 'POST':
        requestBody = JSONParser().parse(request)
        serializeBody = EmployeeSerializer(data=requestBody)
        if serializeBody.is_valid():
            serializeBody.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed Check data",safe = False)

    elif request.method == 'PUT':
        requestBody = JSONParser().parse(request)
        IdtoUpdate = Employee.objects.get(Id = requestBody['Id'])
        serializedEmployeeInfo = EmployeeSerializer(IdtoUpdate, data = requestBody)
        if serializedEmployeeInfo.is_valid():
            serializedEmployeeInfo.save()
            return JsonResponse("Updated Successfully",safe = False)
        return JsonResponse("Updation Failed",safe = False)       



def EmployeeById(request,id):
        if request.method == 'GET':
            employee = Employee.objects.filter(Id = id)
            serializedEmployees = EmployeeSerializer(employee,many = True)
            return JsonResponse(serializedEmployees.data,safe=False)
        elif request.method == 'PUT':
            requestBody = JSONParser().parse(request)
            idtoUpdate = Employee.objects.get(Id =id)
            serializedEmployeeInfo = EmployeeSerializer(idtoUpdate, data = requestBody)
            if serializedEmployeeInfo.is_valid():
                serializedEmployeeInfo.save()
                return JsonResponse("Updated Successfully",safe = False)
            return JsonResponse("Updation Failed",safe = False)
        elif request.method == 'DELETE':
            employeeToDelete = Employee.objects.get(Id = id)
            employeeToDelete.delete()
            return JsonResponse("Deleted Successfully",safe = False)


