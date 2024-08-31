from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from customer.models import customerfeedback,customerticket,customeraddpet

# Create your views here.
def chome(request):
    return render(request,'Customer Home.html')
def cprofile(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Contact = request.POST['Contact']
        Address = request.POST['Address']
        Email = request.POST['Email']
        return render(request,'Customer Profile.html',{'Message':'Successfully Submitted'})
    else:
        return render(request,'Customer Profile.html',{'Message':'Enter Details'})
def caddpet(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Petname = request.POST['Petname']
        Petcolor = request.POST['Petcolor']
        Petage = request.POST['Petage']
        Image = request.POST['Image']
        addDetails = customeraddpet(username=Username,petname=Petname,petcolor=Petcolor,petage=Petage,chooseanimage=Image)
        addDetails.save()
        return render(request,'Customer Add Pet.html',{'Message':'Successfully Submitted'})
    else:
        return render(request,'Customer Add Pet.html',{'Message':'Enter Details'})
def caddedpetlist(request):
    return render(request,'Customer Added Pet List.html')
def cpetlist(request):
    return render(request,'Customer Pet List.html')
def cpetlist1(request):
    return render(request,'Customer Pet List 1.html')
def cbooking(request):
    return render(request,'Customer Booking.html')
def cbookinglist(request):
    return render(request,'Customer Booking List.html')
def chhtlist(request):
    return render(request,'Customer HHT List.html')
def cticket(request):
     if request.method == 'POST':
        Username = request.POST['Userame']
        Hhtname = request.POST['Name']
        Hhttype = request.POST['Type']
        Subject = request.POST['Subject']
        Reason = request.POST['Reason']
        addDetails = customerticket(username=Username,hhtname=Hhtname,type=Hhttype,subject=Subject,reason=Reason)
        addDetails.save()
        return render(request,'Customer Ticket.html',{'Message':'Successfully Submitted'})
     else:
        return render(request,'Customer Ticket.html',{'Message':'Enter Details'})
def cticketlist(request):
    return render(request,'Customer Ticket List.html')
def chistory(request):
    return render(request,'Customer History.html')
def cfeedback(request):
    if request.method == 'POST':
        Username = request.POST['Userame']
        Hhtname = request.POST['hhtname']
        Description = request.POST['Description']
        addDetails = customerfeedback(username=Username,hhtname=Hhtname,description=Description)
        addDetails.save()
        return render(request,'Customer Feedback.html',{'Message':'Successfully Submitted'})
    else:
        return render(request,'Customer Feedback.html',{'Message':'Enter Details'})