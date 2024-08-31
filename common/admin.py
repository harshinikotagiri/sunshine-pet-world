from django.contrib import admin
from django.http.request import HttpRequest
from . import models

# Register your models here.
@admin.register(models.contactform)
class contactform(admin.ModelAdmin):
    list_display = ['name','email','text']

@admin.register(models.adminprofile)
class adminprofile(admin.ModelAdmin):
    list_display = ['name','number','officeaddress','email']

@admin.register(models.adminaddhht)
class adminaddhht(admin.ModelAdmin):
    list_display = ['username','fullname','type','email','phone','experience','description','chooseanimage']

@admin.register(models.registration)
class registration(admin.ModelAdmin):
    list_display = ['username','name','contact','type','email'] 