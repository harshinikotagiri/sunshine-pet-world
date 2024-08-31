from django.urls import path
from . import views
urlpatterns = [
    path('hehome/',views.hehome,name='hehome'),
    path('heprofile/',views.heprofile,name='heprofile'),
    path('hebookinglist/',views.hebookinglist,name='hebookinglist'),
    path('hecustomerlist/',views.hecustomerlist,name='hecustomerlist'),
    path('hepetlist/',views.hepetlist,name='hepetlist'),
    path('hehistory/',views.hehistory,name='hehistory'),
    path('hefeedback/',views.hefeedback,name='hefeedback'),
]