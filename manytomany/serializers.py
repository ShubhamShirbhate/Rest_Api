from rest_framework import serializers
from .models import *


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Module
        fields  = ['id', 'module_name', 'duration', 'class_room']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Student
        fields  = ['id', 'name', 'age', 'grade', 'modules']
        depth = 1