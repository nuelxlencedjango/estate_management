from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

#from django.contrib.auth import get_user_model

#User = get_user_model()



class Customer(models.Model):

    user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='customer')
    phone = models.CharField(max_length=15, null=True,unique=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    state = models.CharField(max_length=50, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    
    class Meta:
        verbose_name_plural = 'Customer' 

    def __str__(self):
        return str(self.user.username)

   
        
        


