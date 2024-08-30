from django.shortcuts import render , get_object_or_404
from rest_framework import viewsets , status
from . models import Student
from . serializers import StudentSerializer
from rest_framework.response import Response
from . pagination import MyPagination , MyLimitPagination , MyCursorPagination
# Create your views here.
class StudentViewset(viewsets.ViewSet):
    pagination_class = MyCursorPagination
    def list(self, request):
        queryset = Student.objects.all()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        print(queryset)
        serializer = StudentSerializer(paginated_queryset , many = True)
        print(serializer.data)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)
    
    def retrieve(self , request , pk = None):
        queryset = Student.objects.all()
        print(queryset)
        stu = get_object_or_404(queryset , pk = pk)
        print(stu)
        serializer = StudentSerializer(stu)
        print(serializer.data)
        return Response(serializer.data)
    
    def create(self , request):
        serializer = StudentSerializer(data =  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self , request , pk = None):
        stu = get_object_or_404(Student , pk = pk)
        serializer = StudentSerializer(stu , data = request.data  , partial  = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk = None):
        stu = get_object_or_404(Student , pk = pk)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        