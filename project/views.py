from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib import messages

from .models import *
from .filters import FilterStudentInfo

#from filters import 
# Create your views here.

# views.py

def home(request):
    return render(request, 'index.html')



def searchStudentInfo(request):
   # student = StudentInfo.objects.all()
    filters = FilterStudentInfo(request.GET, queryset=StudentInfo.objects.all())
    
    context = {"filters":filters}

    return render(request, 'search.html',context)


def employeeSalary(request):
    if request.method =="POST":
        minpay =request.POST.get('minsalary')
        maxpay =request.POST.get('maxsalary')
        resultobj =EmpModel.objects.raw('select empid,empname,email,salary from employee where salary between "'+minpay+'" and "'+maxpay+'"')
        
        context ={
            'resultobj':resultobj
        }
        return render(request,'employee_pay.html',context)
    
    else:
        resultobj =EmpModel.objects.all()
        context ={
            'resultobj':resultobj
        }
        return render(request, 'employee_pay.html',context)


    #minpay =request.POST.get('minsalary')
    #minpay =request.POST.get('minsalary')
    #empobj =EmpModel.objects.all()
    

def availableProperty(request):
    if request.method =="POST":
        name =request.POST.get('property')

        bed =request.POST.get('bedroom')
        bath=request.POST.get('bathroom')

        minpay =request.POST.get('min-price')
        maxpay =request.POST.get('max-price')

        #resultobj =Property.objects.raw('select id, name,price,bedroom,bathroom from Property where price between "'+name+'"  and "'+minpay+'" and "'+maxpay+'" and "'+bed+'" and "'+bath+'" ' )
        resultobj =Property.objects.raw('select id, name,price,bedroom,bathroom from Property where price between "'+minpay+'" and "'+maxpay+'" and "'+bed+'" and "'+bath+'"+"'+name+'" ' )
        
        context ={
            'resultobj':resultobj
        }
        return render(request,'property_info.html',context)
    
    else:
        resultobj =Property.objects.all()
        context ={
            'resultobj':resultobj
        }
        return render(request, 'property_info.html',context)







def team(request):
    return render(request, 'team.html')




def property(request):
    return render(request, 'property.html')




def management(request):
    return render(request, 'management.html')





def marketing(request):
    return render(request, 'marketing.html')





def testimonial(request):
    return render(request, 'testimonial.html')




def contact_us(request):
    return render(request, 'contactus.html')




