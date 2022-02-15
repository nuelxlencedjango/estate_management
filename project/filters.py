from dataclasses import fields
import django_filters
from .models import StudentInfo





class FilterStudentInfo(django_filters.FilterSet):
    class Meta:
        model:StudentInfo
        fields =['student_name','id_no','department','age','cgpa']