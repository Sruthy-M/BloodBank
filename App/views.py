from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,"Login.html")
data={}    
def insert(request):
    name=request.POST['name']
    phone=request.POST['phone']
    Age=request.POST['Age']
    group=request.POST['group']
    data[name]=[phone,Age,group]
    print(data)
    return render(request,"datails.html",{'values':data}) 
users={}
def Signup(request):
    return render(request,"Register.html")
def register(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    users[email]=[name,password]
    print(users)
    return render(request,"Login.html")    
def login(request):
    email=request.POST['email']
    password=request.POST['password']
    print(email,users.items())

    for key,value in users.items():
        if key == email and value[1] == password:
            return render(request,"Reg.html") 
        else:
            return render(request,"Login.html",{"invalid":"invlalid username & password"})    
    
    
            