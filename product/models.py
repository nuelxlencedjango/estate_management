from pydoc import describe
from django.db import models

from django.utils.html import mark_safe
from django.contrib.auth.models import User


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


# Product Model
class Product(models.Model):
    title=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    #specs=models.TextField()
    
    product_size=models.ForeignKey(Size,on_delete=models.CASCADE,default=1)
    status=models.BooleanField(default='Active')
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Products'

    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    #status =models.CharField(max_length=400)
    bedrooms =models.PositiveIntegerField(default=1)
    bathrooms =models.PositiveIntegerField(default=1)
  
   
    subdivision =models.CharField(max_length=400,default='Abuja')

    #color=models.ForeignKey(Color,on_delete=models.CASCADE)
    #size=models.ForeignKey(Size,on_delete=models.CASCADE)
   
    image=models.ImageField(upload_to="product_imgs/",null=True)


    class Meta:
        verbose_name_plural='ProductAttributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

# Order
status_choice=(
        ('process','In Process'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
    )



class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

    class Meta:
        verbose_name_plural='Orders'



# OrderItems
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    image=models.CharField(max_length=200)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='OrderItems'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))

# Product Review
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.review_rating

# WishList
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Wishlist'

# AddressBook
class UserAddressBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50,null=True)
    address=models.TextField()
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='AddressBook'







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
    



	