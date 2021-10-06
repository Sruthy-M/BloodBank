from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Userinfo

def main(request):
    return redirect(login)


def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(display)
        else:
            messages.info(request,'invalid credentials')
            return redirect(login)
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        username    = request.POST['username']
        email_id    = request.POST['email']
        password_1  = request.POST['password1']
        password_2  = request.POST['password2']

        if password_1==password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect(signup)
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,'Email taken')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username,password=password_1,email=email_id,first_name=first_name,last_name=last_name)
                user.save();
                return redirect(login)
               
        else:
            messages.info(request,'password not matching')
            return redirect(login)
        return redirect(signup)
    else:
        return render(request,'signup.html')


def display(request):   
    users = Userinfo.objects.all()
    return render(request,'display.html',{'users':users})


def add_donor(request):
    if request.method == 'POST':
        name              = request.POST['name']
        age               = request.POST['age']
        blood_group       = request.POST['blood_group']
        phone            = request.POST['phone_no']
        unit              = request.POST['unit']
        donation_date     = request.POST['donation_date']

        users = Userinfo.objects.create(name=name,blood_group=blood_group,phone_number=phone,unit=unit,date_of_donation=donation_date,age=age)
        return redirect(display)

    else:
        return render(request,'add_donor.html')


def logout(request):
    auth.logout(request)
    return redirect(login)






