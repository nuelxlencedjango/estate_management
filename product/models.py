from pydoc import describe
from django.db import models

from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField
#from matplotlib.backend_bases import LocationEvent
#from matplotlib.pyplot import title
# Create your models here.





class Property(models.Model):
    name =models.CharField(max_length=200)
    price = models.IntegerField(default=1000)
    bedroom = models.IntegerField(default=1)
    bathroom =models.IntegerField(default=1)
    status =models.CharField(max_length=200,blank=True,null=True) 
    sqft =models.CharField(max_length=10,blank=True,null=True) 
    acre =models.CharField(max_length=10,blank=True,null=True) 
    Location = models.CharField(max_length=200,blank=True,null=True) 
    describe =models.CharField(max_length=200,blank=True,null=True)
    listing_id =models.CharField(max_length=200,blank=True,null=True,unique=True)
    release_date = models.DateField(blank=True,null=True)
    img = CloudinaryField(blank=True,null=True)

    def __str__(self):
        return self.name 

        

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='Property'

    def get_add_to_cart(self):

        return reverse('product:add-to-cart' ,kwargs={
            "pk":self.pk
        })    





class OrderItem(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   product = models.ForeignKey(Property, on_delete=models.CASCADE)
   quantity = models.IntegerField(default =1)
   img = CloudinaryField(blank=True,null=True)
   status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
   description=models.TextField(max_length=100,null=True,blank=True)
   #location = models.ForeignKey('artsans.Area' ,on_delete =models.CASCADE ,null=True,blank=True)
   address = models.CharField(max_length=300, null=True,blank=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   #payment_id
   
   class Meta:
      verbose_name_plural='Orderitem'

   def __str__(self):
      return f"{self.quantity} of {self.product.name}"

   def get_total_item_price(self):
      return self.quantity * self.product.price

   def get_final_price(self):
      return self.get_total_item_price() 

   def vat(self):
      return self.get_vat()   
     



class Order(models.Model):

    #date=models.DateField(auto_now=False,auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    img = CloudinaryField(blank=True,null=True)
    #start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=50,unique=True, default =None,blank=True,null=True)
   
   
    def __str__(self):

        return self.user.username

   
    class Meta:

        verbose_name_plural='Order'
 

    def get_total_price(self):

        total =0
        for order_item in self.items.all():

            total +=order_item.get_final_price()
               

        return total


    def get_total_count(self):

        order =Order.objects.get(pk=self.pk)
        return order.items.count()  

   
    def get_vat(self):

        return (self.get_total_price() * 5)/100

   
    def get_final_amount(self):
        return (self.get_total_price() + self.get_vat()) 








class PropertyImages(models.Model):
    property_details=models.ForeignKey(Property,on_delete=models.CASCADE)
    images_of_property = CloudinaryField('images',blank=True,null=True)
    #description =models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.property_details.name

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='PropertyImages'    







class FeaturedListing(models.Model):
    name =models.CharField(max_length=200)
    price = models.IntegerField(default=1000)
    street_name =models.CharField(max_length=200,blank=True,null=True) 
    location = models.CharField(max_length=200,blank=True,null=True) 
   
    img = CloudinaryField(blank=True,null=True)

    def __str__(self):
        return self.name 

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='FeaturedListing'




class PropertyItems(models.Model):
    name =models.CharField(max_length=200) 
    
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural='PropertyItems'



class Department(models.Model):
    department_name = models.CharField(max_length=200) 

    class Meta:
      verbose_name_plural = "Department"

    def __str__(self):
      return self.department_name




#to be removed
class EmpModel(models.Model):
    empid =models.IntegerField(primary_key=True)
    empname =models.CharField(max_length=100)
    email =models.EmailField()
    salary =models.IntegerField()
   
    def __str__(self):
        return self.empname

    class Meta:
        db_table='employees'    




class StudentInfo(models.Model):
    student_name =  models.CharField(max_length=200) 
    id_no = models.BigIntegerField()
    department =models.ForeignKey(Department,on_delete=models.CASCADE)   
    age =models.IntegerField()
    cgpa =models.DecimalField(max_digits=10,decimal_places=2, default=0.00)  

    def __str__(self):
        return self.student_name










# Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text



# Category
class Category(models.Model):
    title=models.CharField(max_length=100)
    #image=models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='Categories'

    #def image_tag(self):
     #   return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title




# Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='Brands'

    def __str__(self):
        return self.title

# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    sqft =models.IntegerField()
    acres =models.DecimalField(max_digits=10,decimal_places=3, default=0.000)

    class Meta:
        verbose_name_plural='Sizes'

    def __str__(self):
        return self.sqft




class ContactUs(models.Model):

   name = models.CharField(max_length=100) 
   email = models.EmailField(unique = False) 
   phone = models.CharField(max_length=20) 
   selected_properties =models.CharField(max_length=100) 

   message = models.TextField(max_length=200)


   class Meta:
      verbose_name_plural = "Contact Us"

   def __str__(self):
      return self.name  
    

