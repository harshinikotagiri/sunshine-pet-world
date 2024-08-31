from django.urls import path
from . import views
urlpatterns = [
    path('chome/',views.chome,name='chome'),
    path('cprofile/',views.cprofile,name='cprofile'),
    path('caddpet/',views.caddpet,name='caddpet'),
    path('caddedpetlist/',views.caddedpetlist,name='caddedpetlist'),
    path('cpetlist/',views.cpetlist,name='cpetlist'),
    path('cpetlist1/',views.cpetlist1,name='cpetlist1'),
    path('cbooking/',views.cbooking,name='cbooking'),
    path('cbookinglist/',views.cbookinglist,name='cbookinglist'),
    path('chhtlist/',views.chhtlist,name='chhtlist'),
    path('cticket/',views.cticket,name='cticket'),
    path('cticketlist/',views.cticketlist,name='cticketlist'),
    path('chistory/',views.chistory,name='chistory'),
    path('cfeedback/',views.cfeedback,name='cfeedback'),
]