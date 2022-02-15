from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.


admin.site.register(StudentInfo)
admin.site.register(Department)
admin.site.register(Property)
admin.site.register(EmpModel)