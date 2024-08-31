from django.urls import path
from . import views
urlpatterns = [
    path('hahome/',views.hahome,name='hahome'),
    path('haprofile/',views.haprofile,name='haprofile'),
    path('habookinglist/',views.habookinglist,name='habookinglist'),
    path('hacustomerlist/',views.hacustomerlist,name='hacustomerlist'),
    path('hapetlist/',views.hapetlist,name='hapetlist'),
    path('hahistory/',views.hahistory,name='hahistory'),
    path('hafeedback/',views.hafeedback,name='hafeedback'),
]