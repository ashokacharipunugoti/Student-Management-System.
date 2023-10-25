from django.shortcuts import render, redirect
from StudentApp.models import Course, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == "POST":
        user_name = request.POST['tbusername']
        user_password = request.POST['tbpassword']
        myuser = authenticate(username=user_name, password=user_password)
        if myuser is not None:
            if myuser.is_superuser:
                u1 = User.objects.get(username=user_name)
                request.session['myuser'] = u1.id
                request.session['myusername'] = u1.username# based on the id we are getting a details
                login(request, u1)
                return render(request, 'home.html', {'data': u1.username})
            else:
                return render(request,'home.html')

        else:
             return render(request, 'login.html', {'msg': 'credential is not matching!!!'})
    return render(request,'login.html')



def register(request):
    if request.method=='POST':
        uname = request.POST['tbusername']
        useremail = request.POST['tbemail']
        userpswd = request.POST['tbpassword']
        if User.objects.filter(username=uname).exists():
            return render(request, 'register.html', {'user_available': True})
        elif User.objects.filter(email=useremail).exists():
            return render(request,'register.html', {'email_available': True})
        else:
            user = User.objects.create_user(email=useremail, password=userpswd, username=uname)
            user.save()
            return redirect(login)
    return render(request, 'register.html')

   


def home(request):
    students=Student.objects.all()
    return render(request, 'home.html', {'studs':students })
  

    
# Create your views here.
def add(request):
    if request.method=='POST':
        s=Student()
        s.name = request.POST['tbname']
        s.phno = request.POST['tbphno']
        s.email = request.POST['tbemail']
        s.age = request.POST['tbage']
        s.course = Course.objects.get(cname=request.POST['ddlcourse'])
        s.save()
        return redirect(home)
        
    else:
        courses = Course.objects.all()
        data={'courses':courses}
        return render(request, 'addstudent.html', data)
  
    
def edit(request,id):
    s = Student.objects.get(id=id)
    if request.method=="POST":
        s.name = request.POST['tbname']
        s.phno = request.POST['tbphno']
        s.email = request.POST['tbemail']
        s.course = Course.objects.get(cname=request.POST['ddlcourse'])
        s.age = request.POST['tbage']
        s.save()
        return redirect(home)
    else:
        courses=Course.objects.all()
        data = {'student':s, "courses":courses}
        return render (request, 'edit.html',data)
    

def deletefun(request, id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect (home)

def list_of_students(request):
    students=Student.objects.all()
    return render(request, 'list_of_students.html',{'studs':students })