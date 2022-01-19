from lab_6_application.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["idstudent", "first_name", "middle_name", "last_name", "gpa", "image_url"]
