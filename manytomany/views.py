from django.shortcuts import render
from .serializers import ModuleSerializer, StudentSerializer
from rest_framework.response import Response
from .models import Module, Student
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view


'''
class StudentView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        student = Student.objects.all()
        return student


    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Student.objects.create(name=data["name"], age=data["age"], grade=data["grade"], modules=data["modules"])
        new_student.save()

        for module in data["modules"]:
            module_obj = Module.objects.get(module_name=module["module_name"])
            new_student.modules.add(module_obj)

        serializer = StudentSerializer(new_student)
        return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    student = Student.objects.get(id=pk)
    serializer= StudentSerializer(student, many=False)
    return Response(serializer.data)
'''
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        student = Student.objects.all()
        return student
   
    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Student.objects.create(name = data["name"],age = data["age"],grade = data["grade"])
        new_student.save()

        for module in data["modules"]:
            module_obj = Module.objects.get(module_name=module["module_name"])
            new_student.modules.add(module_obj)

        serializer = StudentSerializer(new_student)
        return Response(serializer.data)

    '''

    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Student.objects.create(name=data["name"], age=data['age'], grade=data["grade"])

        new_student.save()

        for module in data["modules"]:
            module_obj = Modules.objects.get(module_name=module["module_name"])
            new_student.modules.add(module_obj)

        serializer = StudentSerializer(new_student)

        return Response(serializer.data)
     '''



class ModulViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        module = Module.objects.all()
        return module
'''

class ModulViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        module = Module.objects.all()
        return module
'''