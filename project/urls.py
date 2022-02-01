from unicodedata import name
from django.urls import path
from .views import *
from . import views




app_name = 'project'
urlpatterns =[
    path('',views.home, name='home'),
    path('our_team/',views.team, name='our_team'),
    path('property/',views.property, name='property'),
    path('management/',views.management, name='management'),
    path('marketing/',views.marketing, name='marketing'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('contactus/',views.contact_us, name='contactus')

    
]