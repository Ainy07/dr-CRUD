from django.contrib import admin
from . models import *
# Register your models here.
@admin.register((Doctor))
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','category','contact','email','password','degree']