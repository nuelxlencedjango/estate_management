
# Create your views here.
from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views

from django.contrib.auth.models import Group
from product.models import *

from .models import *
from .forms import *





#registraion function
def registerPage(request):
    #get forms 
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)
       
        #if form1 and form 2 are without errors
        if form1.is_valid() and form2.is_valid():

            #save form1
            user = form1.save()
             #dont save yet
            profile = form2.save(commit=False)
            #reference user before saving 
            profile.user =user
            profile.save()

            messages.success(request, 'Account successfully created!Please login with your detail ')

            return redirect('accounts:login')

        else:
            messages.success(request, 'Account was Not created for')    
       
    
    form1 =CreateUserForm()
    form2 = CustomerForm()

    context = {'form1':form1, 'form2': form2}   
    return render(request, 'account/register.html', context)





#login function
def loginPage(request):
    if request.method == 'POST':

        #getting login details
        username = request.POST.get('username')
        password =request.POST.get('password')
        #authenticate the user
        user = authenticate(request, username=username, password=password)
        
        #user exists
        if user is not None:
            if Customer.objects.filter(user = user).exists():
                login(request,user)
                return redirect('accounts:dashboard')
            
            # if no such user
            else:
                messages.info(request, 'Information not found! Either Username OR password is incorrect')
    
    return render(request, 'account/login.html')



#dashboard 
def dashboard(request):
    
    # displaying all properties selected by the user in his dashboard
    if Order.objects.filter(user=request.user, ordered =False).exists():
        order = Order.objects.get(user=request.user, ordered=False)

        context={
            'order':order
        }
        return render(request, 'account/dashboard.html',context)
 
    return render(request,'account/dashboard.html')    



#update user information
def update_info(request):
    if request.method =="POST":
        
        # form1 - basic user detail; and form 2- additional information
        form1 = UserUpdateForm(request.POST, instance = request.user)
        form2 = CustomerUpdateForm(request.POST, request.FILES,instance = request.user.customer)
        
        # save if both forms are valid
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

            messages.success(request,"Account Successfully Updated")
            return redirect('product:dashboard')
            
        #if not valid,show warning message   
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form2 = CustomerUpdateForm(instance=request.user.customer)          

    context = {'form1':form1, 'form2':form2}

    return render(request,'account/account_setting.html',context)  



#log out
def logoutPage(request):
    logout(request)
    return redirect('product:home')
