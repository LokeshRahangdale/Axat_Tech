from django import forms
from django.shortcuts import render,redirect
from .forms import Register_Form, ImgForm,TeacherImgForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustUser,student_model,teacher_model
# Create your views here.

def Index_page(request):
    print(request.user)
    return render(request,"authenticate/index.html")

def Register_Stuent_view(request):
    form = Register_Form(request.POST)
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            user1 = form.save()
            CustUser.objects.filter(email=user1).update(is_student=True)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request,email=email, password=password)
            login(request, user)
            print("student")
            messages.success(request, ('You have been Registered'))
            return redirect('index')
        else:
            messages.success(request, ('Somethong went to wrong'))
    return render(request,"authenticate/register_student.html",{"form":form})


def Register_Teacher_view(request):
    form = Register_Form(request.POST)
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            user1 = form.save()
            CustUser.objects.filter(email=user1).update(is_teacher=True)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request,email=email, password=password)
            login(request, user)
            print("teacher")
            messages.success(request, ('You have been Registered'))
            return redirect('index')
        else:
            messages.success(request, ('Somethong went to wrong'))
    return render(request,"authenticate/register_teacher.html",{"form":form})
    

def Logout_View(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out'))
    return redirect('index')

def student_dashboard(request):
    user = request.user
    data = student_model.objects.filter(user=user)
    print(data)
    return render(request,'authenticate/student_dashboard.html',{"data":data})


def teacher_dashboard(request):
    user = request.user
    data = teacher_model.objects.filter(user=user)
    print(data)
    student_img = student_model.objects.all()
    return render(request,'authenticate/teacher_dashboard.html',{"data":data,"student_img":student_img})

def Login_View(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        is_student = CustUser.objects.filter(email = email).values('is_student')[0]['is_student']
        is_teacher = CustUser.objects.filter(email = email).values('is_teacher')[0]['is_teacher']
        if user is not None and is_student:
            login(request, user)
            messages.success(request, ('You have been Logged-in'))
            return redirect('student_dashboard')
        elif user is not None and is_teacher :
            login(request, user)
            messages.success(request, ('You have been Logged-in'))
            return redirect('teacher_dashboard')

        else:
            messages.success(
                request, ('Error While Logging in, Please Try Again'))
            return redirect('index')
    else:
        return render(request, 'authenticate/login.html')
    
def Student_img_view(request):
    if request.method == "POST":
        form = ImgForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            img = form.cleaned_data.get('student_image')
            a = student_model.objects.create(student_image=img,user=user)
            print(img,a)
            data = student_model.objects.filter(user=user)
            print(data)
            messages.success(request, ('Image has been saved'))
            return redirect('student_dashboard')
    return render(request,"authenticate/student_image.html")

def add_teacher_img(request):
    
    if request.method == "POST":
        form = TeacherImgForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = request.user
            img1 = form.cleaned_data.get('image1')
            img2 = form.cleaned_data.get('image2')
            img3 = form.cleaned_data.get('image3')
            teacher_model.objects.create(image1=img1,image2=img2,image3=img3,user=user)
            messages.success(request, ('Images has been saved'))
            return redirect('teacher_dashboard')
        else:
            messages.success(request, ('samething went to wrong'))
    return render(request,"authenticate/teacher_img.html")


def Admin_dashboard(request):
    student_img = student_model.objects.all().order_by("-id")
    teacher_img = teacher_model.objects.all().order_by("-id")
    return render (request,"authenticate/admin_dashboard.html",{"student_img":student_img,"teacher_img":teacher_img})



def Admin_Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        is_superuser = CustUser.objects.filter(email = email).values('is_superuser')[0]['is_superuser']
        if user is not None and is_superuser:
            login(request, user)
            messages.success(request, ('You have been Logged-in'))
            return redirect('admin_dashboard')
        else:
            messages.success(request, ('You have been Logged-in'))
    return render(request,"authenticate/admin_login.html")
