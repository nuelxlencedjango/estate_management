from django.contrib import admin

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