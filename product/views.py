from multiprocessing import context
from pyexpat.errors import messages
from unittest import result
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import *
from django.shortcuts import render ,redirect ,get_object_or_404




def home(request):
    #listing featuredlisting objects
    rented = FeaturedListing.objects.all()

   #get the ip address of visitors,split it where there's (;) comma
    def getIp(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()

        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip 


    #each ip address should be counted once
    ip = getIp(request)
    u = User(visitors=ip)
    result = User.objects.filter(Q(visitors__icontains=ip))
    if len(result) == 1:
        pass
    elif len(result) > 1:
        pass

    else:
        u.save()

    #count the number of visitor
    count = User.objects.all().count()   

    #display
    context={"rented":rented,"count":count}
    return render(request, 'home.html',context)



def availableProperty(request):
    
    #search properties based on  min price and max price
    if request.method =="POST":
        name =request.POST.get('property')
        minpay =request.POST.get('min-price')
        maxpay =request.POST.get('max-price')
        
        # if property chosen is all
        if name == 'all':
            resultobj= Property.objects.filter(price__range=(minpay, maxpay))#.order_by('-price')
         
         #if property chosen is not all
        else:
            resultobj= Property.objects.filter(price__range=(minpay, maxpay),name=name)#.order_by('-price')

        context ={'resultobj':resultobj,}
        return render(request, 'property_info.html',context)  



#search properties in a different page
def propertySearches(request):

    #getting the parameters for search
    if request.method =="POST":
        name =request.POST.get('property')
        minpay =request.POST.get('min-price')
        maxpay =request.POST.get('max-price')

        #if property selected is all
        if name == 'all':
            resultobj= Property.objects.filter(price__range=(minpay, maxpay))#.order_by('-price')
        
        # if property selected is not all
        else:
            resultobj= Property.objects.filter(price__range=(minpay, maxpay),name=name)#.order_by('-price')

        context ={
                'resultobj':resultobj
            }
        
        return render(request, 'search_result.html',context)  




  #image gallery       
def imageGallery(request,id):
    # if property selected exist,store in items or display 404 if not available
    items = get_object_or_404(Property,id=id)

    # admin.StackedInline at work - A model linked to another to posses the properties
    images = PropertyImages.objects.filter(property_details=items)

    number = len(images)
    context={'images':images, 'items':items,'number':number}

    return render(request,'image_gallery.html',context)      


 
 # getting multiple images of the properties          
def featuredImageGallery(request,id):
    items = get_object_or_404(FeaturedListing,id=id)
    images = FeaturedImages.objects.filter(property_details=items)
    number = len(images)
    context={'images':images, 'items':items,'number':number}

    return render(request,'image_gallery.html',context)  


           
def imageSlides(request,id):
    items = get_object_or_404(Property,id=id)
    slide = PropertyImages.objects.filter(property_details=items)
    context={'slide':slide, 'items':items}

    return render(request,'image_slides.html',context)  

   


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



#emai sending from the web
def contact_us(request):
    #select a property 
    items = PropertyItems.objects.all()

    if request.method =='POST':
        #get message ,message tittle,phone number,email address and the property selected
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']
        products = request.POST.getlist('property')

        # seend a mail
        send_mail(
            message_name , # email subject
            #message_phone, #phone no
            message_email , # from email 
            message ,      # main message
            #products, # items

            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
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



def services(request):
    return render(request,'services.html')



#adding to cart for future purchase
def add_to_cart(request, pk):

    #user has to be authenticated
    if request.user.is_authenticated:
        # property id
        product = Property.objects.get(pk=pk)  
    
        #get the property if already exist or create create the  new object
        order_item,created = OrderItem.objects.get_or_create(
            product =product,
            user = request.user,
            ordered = False,
            img = product.img,
            )

        # filter order if it's not ordered by the user    
        order_qs = Order.objects.filter(user=request.user,ordered=False)
        # if available increase the item by 1 and save
        if order_qs.exists():
            order =order_qs[0]
            if order.items.filter(product__pk=pk).exists():
                order_item.quantity +=1

                order_item.save()
                messages.info(request ,"Added additional property successfully")
                return redirect("accounts:dashboard")

            # if not available in the cart,add to order item
            else:
                order.items.add(order_item)
                messages.info(request ," successfully added to your wishlist")
                return redirect("accounts:dashboard")  

        else:
            ordered_date =timezone.now()
            order =Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.info(request,"successfully added to your wishlist")

            return redirect('product:dashboard')          
    

    else:
        messages.info(request,"You need to login to be able to perform this operation")
        return redirect('accounts:login') 
      


#display all products
def allItems(request):
    items = Property.objects.all() 
    
    # pagination 
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 5)
    
    try:
        propertyItems = paginator.page(page)
    except PageNotAnInteger:
        propertyItems = paginator.page(1)
    except EmptyPage:
        propertyItems = paginator.page(paginator.num_pages)

    context ={'propertyItems':propertyItems}

    return render(request,'allProperties.html',context) 







 
 



    