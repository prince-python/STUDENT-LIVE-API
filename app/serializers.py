from rest_framework import serializers
from .models import *


class TeacherSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Teacher
        fields = "__all__"
        
        



class AddStudentsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=AddStudents
        fields = "__all__"
        




class RegistrationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Registration
        fields = "__all__"
        
        
class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields = "__all__"
        