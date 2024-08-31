from django.contrib import admin
from django.http.request import HttpRequest
from . import models

# Register your models here.
@admin.register(models.handlerprofile)
class handlerprofile(admin.ModelAdmin):
    list_display = ['username','name','type','phonenumber','email','experience','description']
