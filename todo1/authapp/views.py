from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_register(request):
    if request.method=="POST":
        #Fetching data
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
        print("Username:",uname)
        print("Password:",upass)
        print("Confirm Password:",ucpass)
        print("email:",uemail)
        u=User.objects.create(username=uname,password=upass,email=uemail)
        u.set_password(upass)#to store password in encrypted format in database.
        u.save()
        return HttpResponse("User Created Successfully")
    else:
      return render(request,'authapp/register.html')
    


    #-----------------------------------------------------------------------------------------
    #to check login (whtr username and password matched or no)

def user_login(request):#whenever the concept of form is used we have to make it/else(POST AND GET METHOD)
   if request.method=="POST": #taking data from user to DB.
    uname=request.POST['uname'] #retrieving data uname,upass 
    #'uname' is the key so alwyz match it with the value from lohin.html.
    upass=request.POST['upass']
    print("Username:",uname)
    print("Password:",upass)

    #concept of authenticate to cross verify the data with db in login
    #authenticate only matches the password wch are in encrypted format and u WILL TAKE CMPLT ROW DATA IN IT
    u=authenticate(username=uname,password=upass)
    #print("User object:",u)#u holds the entire details of that login.complete row
    #print("ID:",u.id)#id,username are all column names from db 
    #print("Username:",u.username)
    #print("Password:",u.password)
    #print("Email:",u.email)
    #print("Superuser:",u.is_superuser)

    if u is not None:
       login(request,u)
       return redirect('/home')
    else:
       context={}#we need to make changes in 
       context['errmsg']="Invalid Username or Password"
       return render(request,'authapp/login.html',context)
       #return HttpResponse("Invalid Username or Password")
    
    
    
   else:
      return render(request,'authapp/login.html')