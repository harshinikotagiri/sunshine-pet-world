from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from handler.models import handlerprofile

# Create your views here.
def hahome(request):
    return render(request,'Handler Home.html')
def haprofile(request):
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
        return render(request,'Handler Profile.html',{'Message':'Successfull Submitted'})
    else:
        return render(request,'Handler Profile.html',{'Message':'Enter Details'})
def habookinglist(request):
    return render(request,'Handler Booking List.html')
def hacustomerlist(request):
    return render(request,'Handler Customer List.html')
def hapetlist(request):
    return render(request,'Handler Pet List.html')
def hahistory(request):
    return render(request,'Handler History.html')
def hafeedback(request):
    return render(request,'Handler Feedback.html')

