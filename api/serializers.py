from rest_framework import serializers
from students.models import Student


class Studentseriallizer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields="__all__"