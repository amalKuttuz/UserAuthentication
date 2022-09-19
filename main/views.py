from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        email=request.POST['email']
        password2=request.POST['password2']
        first_name=request.POST['first_name']
        if(password1==password2):

            Myuser=User.objects.create_user(username,email,password2)
            Myuser.first_name=first_name
            Myuser.save()
            messages.success(request, "New account has been created sucessfully")
            return redirect('signin')
        else:
            messages.error(request,"passwords doesn't match")
            return redirect("signup")
    return render(request,'signup.html')

def signin(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            firstname=user.username
            messages.success(request, "Logged in sucessfully")

            return render(request,"userdashboard.html",{'username':username})
        else:
            messages.error(request, "Invalid credentials")
            return redirect("signin")
    return render(request,"signin.html")

# def userdashboard(request):
    # if request.method==('POST'):
    #     address=request.POST['address']
    #     phno=request.POST['phno']
    #     Myuser.address=address
    #     Myuser.phno=phno
    #     Myuser.save()
    #     messages.success(request, "data's has been saved sucessfully")
    #     return redirect('userdashboard')


    # return render(request,'userdashboard.html',{'Myuser.phno',Myuser.phno})

def signout(request):
    logout(request)
    messages.success(request, "sucessfully logged out")
    return render(request, "signin.html")
