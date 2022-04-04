from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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

       # bed =request.POST.get('bedroom')
        #bath=request.POST.get('bathroom')

        minpay =int(request.POST.get('min-price'))
        maxpay =int(request.POST.get('max-price'))

        #resultobj =Property.objects.raw('select id, name,price,bedroom,bathroom from Property where price between "'+name+'"  and "'+minpay+'" and "'+maxpay+'" and "'+bed+'" and "'+bath+'" ' )
        #resultobj =Property.objects.raw('select id, name,price,bedroom,bathroom from accomodation where price between "'+minpay+'" and "'+maxpay+'"  ' )
        #resultobj =EmpModel.objects.raw('select empid,empname,email,salary from employee where salary between "'+minpay+'" and "'+maxpay+'"')
        if name == 'all':
            resultobj= Property.objects.filter(price__range=(minpay, maxpay))

            context ={ 'resultobj':resultobj}
            return render(request,'property_info.html',context)
        
        else:

            resultobj= Property.objects.filter(price__range=(minpay, maxpay),name=name)

            context ={ 'resultobj':resultobj}
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
    items = PropertyItems.objects.all()

    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']
       # products_name =request.POST['property']
        products = request.POST.getlist('property')




        # seend a mail
        # the order in which  to  pass arugument in the parameters is important
        send_mail(
            message_name , # email subject
            #message_phone, #phone no
            message_email , # from email 
            message ,      # main message
            #products, # items

            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.selected_properties = products
        contacts.message = message
        contacts.save()


        return render(request ,'email.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contactus.html', {'items':items}) 



    #ns =['manago','banana','orange','apple','cashew','groundnut']
    #if request.method =='POST':
     #   fruits = request.POST.getlist('ns')
      #  print(fruits)
       # if fruits == 'manago':
        #    print('you selected manago')

    #return render(request, 'contactus.html')*/




def services(request):
    return render(request,'services.html')


