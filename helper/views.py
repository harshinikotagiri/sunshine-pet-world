from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from helper.models import helperprofile

# Create your views here.
def hehome(request):
    return render(request,'Helper Home.html')
def heprofile(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Name = request.POST['Name']
        Type = request.POST['Type']
        Phonenum = request.POST['Phonenum']
        Email = request.POST['Email']
        Experience = request.POST['Experience']
        Description = request.POST['Description']
        addDetails = handlerprofile(username=Username,name=Name,type=Type,phonenum=Phonenum,email=Email,experience=Experience,description=Description)
        addDetails.save()
        return render(request,'Helper Profile.html',{'Message':'Successfull Submitted'})
    else:
        return render(request,'Helper Profile.html',{'Message':'Enter Details'})
def hebookinglist(request):
    return render(request,'Helper Booking List.html')
def hecustomerlist(request):
    return render(request,'Helper Customer List.html')
def hepetlist(request):
    return render(request,'Helper Pet List.html')
def hehistory(request):
    return render(request,'Helper History.html')
def hefeedback(request):
    return render(request,'Helper Feedback.html')
