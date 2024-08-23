from django.contrib import admin
from .models import *

# Register your models here.


class StaffInfo(admin.ModelAdmin):
    list_display=('first_name','last_name', 'role','contact_no',)
admin.site.register(Staff, StaffInfo)
