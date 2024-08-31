from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'), 
    path('gallery/',views.gallery,name='gallery'),
    path('login',views.customlogin,name='login'), 
    path('registration/',views.cregistration,name='registration'),
    path('admn/',views.admn,name='admn'),
    path('customer/',views.customer,name='customer'),
    path('handler/',views.handler,name='handler'),
    path('helper/',views.helper,name='helper'),
    path('trainer/',views.trainer,name='trainer'),
    path('logout/',views.logouts,name='logout'),
]