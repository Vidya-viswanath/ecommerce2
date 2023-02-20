from django.shortcuts import render
from . serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Student
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')
# Create your views here.


@api_view(['POST'])
def add_student(request):
    logger.info("this is info message")


    params = request.data
    serialized_data = StudentSerializer(data = params)

    if serialized_data.is_valid() :
        serialized_data.save()
        return Response({'statusCode': 201,'msg': 'Student Added Successfully'})

    else :
         return Response({'statusCode': 500,'msg': 'Form Error'})


@api_view(['GET'])
def list_student(request) : 
    student = Student.objects.all()
    serialized_data = StudentSerializer(student,many = True) 
    return Response({'students':serialized_data.data})


@api_view(['DELETE'])
def delete_student(request,sid) :
    try :
     student = Student.objects.get(id = sid)
     student.delete()
    except : 
        return Response({'statusCode': 404,'msg': 'Student Not Found'})

    return Response({'statusCode': 200,'msg': 'Student Deleted Successfully'})



@api_view(['PUT'])
def update_student(request,sid) :
    params = request.data
    student = Student.objects.get(id = sid)
    serialized_data = StudentSerializer(student, data = params)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response({'statusCode': 200,'msg': 'Data Updated Successfully'})
    else :
        return Response({'statusCode': 500,'msg': 'Form Error'})

@api_view(['GET'])
def index(request) :
    return Response('congratulations, you have created an API')


@api_view(['GET'])
def home(request) :
    return Response(3.90)


    
         
