#from dataclasses import fields
from pyexpat import model
import django_filters
from .models import *





class FilterStudentInfo(django_filters.FilterSet):
    class Meta:
        model:StudentInfo
        fields =['student_name','id_no','department','age','cgpa']



class PropertyFilters(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model:Property
        fields =['price','name']#,'bedroom','bathroom','listing_id','Location']





#class ProductFilter(django_filters.FilterSet):
#    price = django_filters.NumberFilter()
 #   price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
 #   price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

 #   release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
  #  release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
 #   release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

  #  manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

  #  class Meta:
  #      model = Product