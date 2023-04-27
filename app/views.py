from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class = TeacherSerializers
    
    


class AddStudentViewSet(viewsets.ModelViewSet):
    queryset=AddStudents.objects.all()
    serializer_class =AddStudentsSerializers
    
  
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset=Registration.objects.all()
    serializer_class =RegistrationSerializers
    
    
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class =  CourseSerializers