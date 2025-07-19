from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import Studentseriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["GET"])
def studentviews(request):
    if request.method=='GET':
     Students=Student.objects.all()
     serializers=Studentseriallizer(Students,many=True)
    return Response(serializers.data)
    
          

