from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from trainer.models import trainerprofile

# Create your views here.
def thome(request):
    return render(request,'Trainer Home.html')
def tprofile(request):
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
        return render(request,'Trainer Profile.html',{'Message':'Successfull Submitted'})
    else:
        return render(request,'Trainer Profile.html',{'Message':'Enter Details'})
def tbookinglist(request):
    return render(request,'Trainer Booking List.html')
def tcustomerlist(request):
    return render(request,'Trainer Customer List.html')
def tpetlist(request):
    return render(request,'Trainer Pet List.html')
def thistory(request):
    return render(request,'Trainer History.html')
def tfeedback(request):
    return render(request,'Trainer Feedback.html')
