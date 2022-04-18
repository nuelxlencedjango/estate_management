
# Create your views here.
from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
#from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import views as auth_views

from django.contrib.auth.models import Group
from product.models import *

from .models import *
from .forms import *






def registerPage(request):
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)
        #item = request.POST.get('result.id')

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.user =user
            profile.save()

            #id = form1.cleaned_data.get('id')

            messages.success(request, 'Account successfully created!Please login with your detail ')

            return redirect('accounts:login')

        else:
            messages.success(request, 'Account was Not created for')    
       
    
    form1 =CreateUserForm()
    form2 = CustomerForm()

    context = {'form1':form1, 'form2': form2}   
    return render(request, 'account/register.html', context)





#@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            if Customer.objects.filter(user = user).exists():
                login(request,user)
                return redirect('accounts:dashboard')
           
            else:
                messages.info(request, 'Information not found! Either Username OR password is incorrect')
    

    
    return render(request, 'account/login.html')




def dashboard(request):

    if Order.objects.filter(user=request.user, ordered =False).exists():
        order = Order.objects.get(user=request.user, ordered=False)
        context={
            'order':order
        }
        return render(request, 'account/dashboard.html.html',context)

    messages.info(request, 'You have no order in your wishlist')   
    return render(request,'account/dashboard.html.html')    









def update_info(request):
    if request.method =="POST":

        form1 = UserUpdateForm(request.POST, instance = request.user)
        form2 = CustomerUpdateForm(request.POST, request.FILES,instance = request.user.customer)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

            messages.success(request,"Successfully updated")
            return redirect('products:dashboard')
            
           
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form2 = CustomerUpdateForm(instance=request.user.customer)          

    context = {'form1':form1, 'form2':form2}

    return render(request,'account/update_info.html',context)  




def logoutPage(request):
    logout(request)
    return redirect('products:home')
