from django.contrib import admin
from numpy import product

# Register your models here.

from .models import *
# Register your models here.


# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User




admin.site.register(StudentInfo)
admin.site.register(Department)
admin.site.register(Property)
admin.site.register(EmpModel)



admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(Category)
admin.site.register(Size)

