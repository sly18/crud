from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  .models import Students


def Home(request):
    data=Students.objects.all()
    contex={"data":data}
    return render(request, 'index.html',contex)


def edit(request):
    return render(request, 'edit.html')


def login(request):
    return render(request, 'login.html')


def signup(request):

    return render(request, 'signup.html')


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        query=Students(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request, 'index.html')


def updateData(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        edit=Students.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=Students.objects.get(id=id)
    context={'d':d}
    return render(request,'edit.html',context)


def deleteData(request,id):
    d=Students.objects.get(id=id)
    d.delete()
    return redirect('/')
    return render(request,'index.html')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')

        else:
            return redirect('/login')

    return render(request, "login.html")




def handlesignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        myuser = User.objects.create_user(username, password)
        myuser.save()
    return render(request, "signup.html")




def handlelogout(request):
    logout(request)
    return redirect('/signup')

