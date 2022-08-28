from django.contrib import admin
from numpy import product

# Register your models here.

from .models import *




# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','selected_properties', 'message']



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','items','img','ordered_date', 'ordered','order_id']



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','status', 'description','address','date_created']



class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImages

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
       model = Property

@admin.register(PropertyImages)
class PropertyImageAdmin(admin.ModelAdmin):
    pass



admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(PropertyItems)
#admin.site.register(FeaturedListing)
admin.site.register(OurTeam)




class FeaturedImageAdmin(admin.StackedInline):
    model = FeaturedImages

@admin.register(FeaturedListing)
class  FeaturedListingAdmin(admin.ModelAdmin):
    inlines = [FeaturedImageAdmin]

    class Meta:
       model = FeaturedListing

@admin.register(FeaturedImages)
class FeaturedImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)