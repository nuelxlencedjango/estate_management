from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from .filters import FilterStudentInfo
from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)

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
#class availableProperty(ListView):
  #  model = Property
   # template_name = 'property_info.html'  # Default: <app_label>/<model_name>_list.html
  #  context_object_name = 'resultobj'  # Default: object_list
  #  paginate_by = 10
   # queryset = User.objects.all()  # Default: Model.objects.all()


def product_list_view(request):
    qs = product.objects.all()
    location_search = request.GET.get('location')
    categories = request.GET.get('categories')
    price = request.GET.get('price')

    if location_search:
        qs = qs.filter(location__contains=location_search)
    qs = qs.order_by('-pub_date')
    paginator = Paginator(qs, 5)
    page = p.page(request.GET.get('page'))
    context = {
       'posts': page
      }

    return render(request, "products/product_list.html", context)



def availableProperty(request):
    if request.method =="POST":

        name =request.POST.get('property')
        minpay =request.POST.get('min-price')
        maxpay =request.POST.get('max-price')

        if name == 'all':
            result= Property.objects.filter(price__range=(minpay, maxpay))#.order_by('-price')

        else:
            result= Property.objects.filter(price__range=(minpay, maxpay),name=name)#.order_by('-price')
           
        try:
            p = Paginator(result,5)
            number = request.GET.get('page',1)
            resultobj = p.get_page(number)

        
        except PageNotAnInteger:
                resultobj = p.get_page(1)
        except EmptyPage:

            resultobj = p.get_page(p.num_pages)   

        context ={
            'resultobj':resultobj
        }
        return render(request, 'property_info.html',context)     

    
    context ={
            'resultobj':resultobj
        }
    return render(request, 'property_info.html',context)    


   
def availablePropertypp(request):
    if request.method =="GET":

        name =request.POST.get('property')
        minpay =request.POST.get('min-price')
        maxpay =request.POST.get('max-price')

        if name == 'all':

            result= Property.objects.filter(price__range=(minpay, maxpay))#.order_by('-price')


            #items = Property.objects.all()
            p = Paginator(result,5)
            number = request.GET.get('page',1)
            resultobj = p.get_page(number)

            context ={ 'resultobj':resultobj}
            return render(request,'property_info.html',context)


       


    context ={ 'resultobj':resultobj}
    return render(request,'property_info.html',context)
    


def availablePropertylp(request):

    if request.method =="GET":
        name =request.POST.get('property')

       # bed =request.POST.get('bedroom')
        #bath=request.POST.get('bathroom')

        minpay =int(request.POST.get('min-price'))
        maxpay =int(request.POST.get('max-price'))


        if name == 'all':
            result= Property.objects.filter(price__range=(minpay, maxpay)).order_by('-price')

            #pagination
            page_number = request.GET.get('page')
            paginator = Paginator(result, 10)

            try:
               #users = paginator.page(page)
               resultobj = paginator.get_page(page_number)
            except PageNotAnInteger:
                resultobj = paginator.get_page(1)
            except EmptyPage:

                resultobj = paginator.get_page(paginator.num_pages)
            
                #resultobj = paginator.get_page(page_number)

            

            context ={ 'resultobj':resultobj}
            return render(request,'property_info.html',context)
        
        else:

            result= Property.objects.filter(price__range=(minpay, maxpay),name=name).order_by('-price')
            page_number = request.GET.get('page')
            paginator = Paginator(result, 10)

            try:
                resultobj = paginator.get_page(page_number)
            except PageNotAnInteger:
                resultobj = paginator.get_page(1)

            except EmptyPage:
                resultobj = paginator.get_page(paginator.num_pages)
            
           
            

            context ={ 'resultobj':resultobj}
            return render(request,'property_info.html',context)
    

    else:
        resultobj =Property.objects.all().order_by('-price')
        page_number = request.GET.get('page')
        paginator = Paginator(result, 10)
        try:
            resultobj = paginator.get_page(page_number)
        except PageNotAnInteger:

            resultobj = paginator.get_page(1)
        except EmptyPage:
            resultobj = paginator.get_page(paginator.num_pages)  

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



