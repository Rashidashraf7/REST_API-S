from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import Studentseriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["GET","POST"])
def studentviews(request):
    if request.method=='GET':
     Students=Student.objects.all()
     serializers=Studentseriallizer(Students,many=True)
     return Response(serializers.data)
    elif request.method=='POST':
        data=request.data
        serializers=Studentseriallizer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
@api_view(['GET','PUT']) 
def update(request, pk):
   
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})
    
    if request.method=='GET':
        serializers=Studentseriallizer(student)
        return Response(serializers.data)
    elif request.method=="PUT":
        data=request.data
        serializers=Studentseriallizer(student,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
       
    

    
        

        
    
           

