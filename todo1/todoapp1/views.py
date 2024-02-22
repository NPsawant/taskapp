from django.shortcuts import render,HttpResponse,redirect
from todoapp1.models import Tasklist1

# Create your views here.
def contact_page(request):
    return HttpResponse("Hello from Contact page!!!")
    #return redirect ('/about')

def about_page(request):
    return HttpResponse("Hy Welcome !!!know more About us")


def products_page(request):
    return HttpResponse("welcome to page of products!!!")

def awards_page(request):
    return HttpResponse("<h1>Awards and Recognition</h1>")

def home_page(request):
    #return HttpResponse("welcome to Home_page!!!")
    #return redirect('/about')

    #t=Tasklist1.objects.all() # select * from  todoapp_tasklist; all objects can be seen in single line.
    t=Tasklist1.objects.filter(is_active=1)#for soft delete concept we make *filter(is_active=1)*
    #dashboard.HTML table file will be displayed on screen
    print (t) #this will print on the CMD screen
    print (request.user)#once the data stored in session.

    #to access all the objects to show on the screen make use of for loop

    for x in t: #accessing each object [obj1 ,obj 2 ,obj 3, obj 4]
        print(x) #all the data goes into x and gets printed. IN CMD

        print("ID:",x.id)
        print("TITLE :",x.title)
        print("DETAILS :",x.detail)
        print("DUE_DATE :",x.due_dt)
        print("IS_COMPLETED :",x.is_completed)
        print("IS_ACTIVE :",x.is_active)
        print()

        #to print the above data on screen concept of context is used {dictionary}
    context={} #create a empty dictionary.
    context['data']=t #This (data) is key which contains all the objects.


    return render(request,'todoapp1/dashboard.html',context) #add context in the at the end 
   # return render(request,'todoapp1/dashboard.html')

#To check the view at frontend on screeen we did the below operations.
def dtl(request):
    context={} #Always create a empty dictionay {'key':value} pair
    context['a']=20
    context['user']="Nivedita"
    context['b']=50
    context['l']=[10,20,30,40,50,60]
    return render(request,'todoapp1/dashboard.html',context) 



def add_task(request):
    print("METHOD TYPE:",request.method)
    #return render(request,'todoapp1/addtask.html')#Before object is created 
    if request.method=="POST":
        print("In If section")
        #return HttpResponse("Insert data into database")

        #FETCH FROM file on screen 
        t=request.POST['title']
        d=request.POST['det']
        dt=request.POST['duedt']
        print("Title:",t)
        print("Details:",d)
        print("Date:",dt)
        t=Tasklist1.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user)#object created
        t.save()#object saved
        #return HttpResponse("Data Fetched from the form") #previously we were getting this bfr data insertion
        #return HttpResponse("Data inserted successfully into database") #(this page with the comment would be opened after filling the data)
        return redirect('/home') #redirect is used after adding data will be redirected to the home page.
    else:
        print("In Else section")
        return render(request,'todoapp1/addtask.html')
    

    #concept of delete ##from the screen dashboard we shud be able to delete it 

def delete_task(request,rid):#Add the same parameter rid given in the url anglo bracket<>
        #print("ID to be deleted:",rid)#To cross check we print this and chck ONLY IT SHOW TO BE DELETED BUT DOES NOT DELETE
        #return HttpResponse("ID TO BE DELETED:"+rid)#+ concatenation to show on screen (ID TO BE DELETED:1
        #t=Tasklist1.objects.get(id=rid)#DATA TO BE DELETED IS FETCHED 
        #print(t)
        #return HttpResponse("Record Fetched")
        #t.delete()#NOW THE DATA FETCHED WILL BE DELETED PERMANENTLY
        #return HttpResponse("Object deleted") #HERE IT SHOWS THAT THE DATA DELETED IT SI HARD DELETE BACKEND DATA IS DELETED
        t=Tasklist1.objects.filter(id=rid)##soft delete so we are using update in the delete .
        t.update(is_active=0)
        return redirect("/home") #NOW THE DATA IS DELETED AND RETURN BACK TO HOME PAGE

    #concept of EDIT ##from the screen dashboard we shud be able to EDIT it

def edit_task(request,rid):
    print("ID to be edited:",rid)
    #return HttpResponse("ID TO BE EDITED:"+rid)
    if request.method =="POST":
        ut=request.POST['title']
        ud=request.POST['det']
        udt=request.POST['duedt']
        print("Updates Title:",ut)
        print("Updated Details:",ud)
        print("Updated Date:",udt)
        t=Tasklist1.objects.filter(id=rid)
        t.update(title=ut,detail=ud,due_dt=udt)
        #return HttpResponse("Details Fetched")
        return redirect("/home")
        
    else:
        t=Tasklist1.objects.get(id=rid)
        context={}
        context['data']=t
        return render(request,'todoapp1/editform.html',context) 
    #editform is made used ,it is existing/addtask form where value attributes are added and then after filling
    #and submitting it becomes post method data is fetched from html to backend


def mark_completed(request,rid):
    t=Tasklist1.objects.filter(id=rid)
    t.update(is_completed=1)
    
    return redirect('/home')
