from unicodedata import name
from django.urls import path
from .views import *
from . import views




app_name = 'product'
urlpatterns =[
    path('',views.home, name='home'),
    path('our_team/',views.team, name='our_team'),
    path('property/',views.property, name='property'),
    path('management/',views.management, name='management'),
    path('marketing/',views.marketing, name='marketing'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('contactus/',views.contact_us, name='contactus'),


    path('search/',views.searchStudentInfo,name='search'),
    path('employee/', views.employeeSalary, name='employee'),


    
   # path('property_search/' ,views.availableProperty,name='property_search'),

    path('property_search/' ,ItemsListView ,name="property_search"),



    path('services/',views.services,name='services'),

    
]

