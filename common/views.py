from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from common.models import registration,contactform

# Create your views here.
def home(request):
    return render(request,'Home.html')
def contact(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Text = request.POST['Text']
        addDetails = contactform(name=Name,email=Email,text=Text)
        addDetails.save()
        return render(request,'Contact.html',{'Message':'Successfully Submitted'})
    else:
         return render(request,'Contact.html',{'Message':'Enter Details'})
def service(request):
    return render(request,'Service.html')
def gallery(request):
    return render(request,'Gallery.html')
def customlogin(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/')
         
        user = authenticate(username=username,password=password)
         
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/')
        else:
            ur = registration.objects.get(username=username)
            if ur.type == "Customer":
                login(request, user)
                return redirect('customer/chome')
            elif ur.type == "Handler":
                login(request, user)
                return redirect('handler/hahome')
            elif ur.type == "Helper":
                login(request, user)
                return redirect('helper/hehome')
            else:
                login(request, user)
                return redirect('trainer/thome')
    return render(request,"Login.html",{'message':'password did not match'})
def cregistration(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Name = request.POST['Name']
        Contact = request.POST['Contact']
        Type = request.POST['role']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Confirmpassword = request.POST['Confirmpassword']
        if Password == Confirmpassword:
            user = User.objects.filter(username=Username)
            if user.exists():
                messages.info(request, "Username already taken!")
                return redirect('/registration')
            user = User.objects.create_user(
            first_name=Name,
            username=Username
            )
            user.set_password(Password)
            user.save()
            addDetails = registration(username=Username,name=Name,contact=Contact,type=Type,email=Email)
            addDetails.save()
            messages.info(request, "Account created Successfully!")
            return redirect('/login')
    else:
        return render(request,"Registration.html",{'message':'password did not match'})
def admn(request):
    return render(request,'Admin.html')
def customer(request):
    return render(request,'Customer.html')
def handler(request):
    return render(request,'Handler.html')
def helper(request):
    return render(request,'Helper.html')
def trainer(request):
    return render(request,'Trainer.html')
def logouts(request):
    logout(request)
    return redirect('/')
