from django.urls import path
from . import views
urlpatterns = [
    path('thome/',views.thome,name='thome'),
    path('tprofile/',views.tprofile,name='tprofile'),
    path('tbookinglist/',views.tbookinglist,name='tbookinglist'),
    path('tcustomerlist/',views.tcustomerlist,name='tcustomerlist'),
    path('tpetlist/',views.tpetlist,name='tpetlist'), 
    path('thistory/',views.thistory,name='thistory'),
    path('tfeedback/',views.tfeedback,name='tfeedback'),  
]
    