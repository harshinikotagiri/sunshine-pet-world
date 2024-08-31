from django.contrib import admin
from django.http.request import HttpRequest
from . import models

# Register your models here.
@admin.register(models.customeraddpet)
class customeraddpet(admin.ModelAdmin):
    list_display = ['username','petname','petcolor','petage','chooseanimage']
    list_filter = ['pettype','petbreed','petgender']

@admin.register(models.customerbooking)
class customerbooking(admin.ModelAdmin):
    list_display = ['bookingid','customerusername','hhtusername','status']

@admin.register(models.customerticket)
class customerticket(admin.ModelAdmin):
    list_display = ['username','hhtname','type','subject','reason','reply']

@admin.register(models.customerfeedback)
class customerfeedback(admin.ModelAdmin):
    list_display = ['username','hhtname','subject','description']

