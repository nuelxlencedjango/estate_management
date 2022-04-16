from django.urls import path
from .views import *
from .import views

from django.contrib.auth import views as auth_views



app_name = 'accounts'


urlpatterns = [
   
  
    path('register/',views.registerPage,name ='register'),

     path('dashboard/',views.dashboard,name ='dashboard'),
  
    path('login/' ,views.loginPage , name='login'),
  
    path('update_info/', views.update_info, name="update_info"),
   
    path('logout/', views.logoutPage, name='logout'),
  

    
]
