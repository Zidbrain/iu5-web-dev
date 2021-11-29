from django.shortcuts import render
from rest_framework import viewsets
from lab_6_application.serializers import StudentSerializer
from lab_6_application.models import Student

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
