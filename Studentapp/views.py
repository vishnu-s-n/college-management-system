import email
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
import random
from django.conf import settings



# def send_otp_email(e):
#     subject= 'TakeANo Acount Verification email'
#     otp = random.randint (100000, 999999)
#     message = f'your otp is {otp}'
#     email_from=settings.EMAIL_HOST_USER
#     send_mail(subject, message, email_from , [e])
#     u=teachers.objects.get(email = e)
#     print(u)
#     u.log_otp= otp
#     u.save()


# def student_send_otp_email(e):
#     subject= 'TakeANo Acount Verification email'
#     otp = random.randint (100000, 999999)
#     message = f'your otp is {otp}'
#     email_from=settings.EMAIL_HOST_USER
#     send_mail(subject, message, email_from , [e])
#     u=student.objects.get(em = e)
#     print(u)
#     u.otp= otp
#     u.save()

# #admin signup
# def signup(request):
#     if request.method=="POST":
#         fn=request.POST.get('fname')
#         ln=request.POST.get('lname')
#         em=request.POST.get('email')
#         us=request.POST.get('username')
#         pw=request.POST.get('password')
#         User.objects.create_user(first_name=fn,last_name=ln,username=us,email=em,password=pw)
#         return render(request,"frontpages/index.html")
#     return render(request,"frontpages/signup.html")

# #admin login
# def login_user(request):
#     if request.method=="POST":
#         em=request.POST.get('email')
#         pw=request.POST.get('password')
#         user=authenticate(request,email=em,password=pw)
#         if user:
#             login(request,user)
#             return render(request,"Dashboard/index2.html")
#         else:
#            return HttpResponse("Invalid User!!")
#     return render(request,"frontpages/login.html")

# #admin logout    
# def logout_user(request):
#     logout(request)
#     return redirect('home')

#front pages
def home(request):
    return render(request,"frontpages/index.html")

def userhome(request):
    return render(request,"frontpages/userindex.html")

def teacherslist(request):
    return render(request,"Dashboard/teachers.html")

def courselist(request):
    return render(request,"Dashboard/courses.html")

# #teacher module
# def addteacher(request):
#     dep=department.objects.all()
#     if request.method=='POST':
#         f=request.POST.get('fname')
#         l=request.POST.get('lname')
#         d=request.POST.get('department')
#         e=request.POST.get('email')
#         ph=request.POST.get('mobile')
#         im=request.FILES['img']
#         fo=FileSystemStorage()
#         im2=fo.save(im.name,im)
#         de=department.objects.get(id=d)
#         if teachers.objects.filter(email=e).exists():
#             return HttpResponse("Already Exist!!")
#         else:
#             teachers.objects.create(fname=f,lname=l,email=e,mob=ph,dname=de,profile_pic=im2)
#             send_otp_email(e)
#     return render(request,"Dashboard/addteacher.html",{"data":dep})


# def getteachers(request):
#     k=teachers.objects.all()
#     if request.method=="POST":
#         se=request.POST.get('name')
#         res=teachers.objects.filter(name=se)
#         return render(request,"Dashboard/list.html",{"data":res})
#     return render(request,"Dashboard/list.html",{"data":k})


# def delteacher(request,userid):
#     o=teachers.objects.get(id=userid)
#     o.delete()
#     return redirect("all")

# def update_teacher(request,userid):
#     x=teachers.objects.filter(id=userid).values()
#     k=department.objects.all()
#     if request.method=="POST":
#         F=request.POST.get('fname')
#         L=request.POST.get('lname')
#         M=request.POST.get('mobile')
#         E=request.POST.get('email') 
#         D=request.POST.get('department')
#         P=request.POST.get('password')  
#         x.update(fname=F,lname=L,mob=M,email=E,dname=D,pas=P)
#         return redirect("all")
#     return render(request,"Dashboard/edit.html",{"userdata":x[0],"id":userid,"data":k})

# def teacher_log(request):
#     if request.method=="POST":
#         em=request.POST.get('email')
#         p=request.POST.get('password')
#         if teachers.objects.filter(email=em,log_otp=p).exists():
#             k=teachers.objects.filter(email=em,log_otp=p).values().first() 
#             request.session["fname"]=k["fname"]
#             request.session["email"]=k["email"]
#             request.session['img']=k['profile_pic']
#             return render(request,"Dashboard/staffindex.html")
#         else:
#            return HttpResponse("Invalid User!!")
#     return render(request,"frontpages/tlogin.html")


# def logout_teacher(request):
#     return redirect('home')

# def teacher_profile(request):
#     em=email                                    
#     k1=teachers.objects.filter(email=em).values()
#     print(k1)
#     return render(request,"Dashboard/Profile.html")

# #student module
# def login_student(request):
#     if request.method=="POST":
#         e=request.POST.get('email')
#         pa=request.POST.get('password')
#         if student.objects.filter(em=e,otp=pa).exists():
#             k=student.objects.filter(em=e,otp=pa).values().first() 
#             request.session["fname"]=k["fname"]
#             request.session["email"]=k["em"]
#             return render(request,"frontpages/userindex.html")
#         else:
#            return HttpResponse("Invalid Id!!")
#     return render(request,"frontpages/studlogin.html")


# def logout_student(request):
#     if 'email' in request.session:
#         logout(request)
#         return redirect('slogin')
#     else:
#         return redirect('slogin')



# def addstudents(request):
#     a=department.objects.all()
#     b=teachers.objects.all()
#     if request.method=='POST':
#         f=request.POST.get('fname')
#         l=request.POST.get('lname')
#         d=request.POST.get('department')
#         e=request.POST.get('email')
#         ph=request.POST.get('mobile')
#         im=request.FILES['img']
#         fo=FileSystemStorage()
#         im2=fo.save(im.name,im)
#         te=request.POST.get('teacher')
#         de=department.objects.get(id=d)
#         tea=teachers.objects.get(id=te)
#         if student.objects.filter(em=e).exists():
#             return HttpResponse("Already Exist!!")
#         else:
#             student.objects.create(fname=f,lname=l,em=e,mob=ph,dname=de,tuitor=tea,profile_pic=im2)
#             student_send_otp_email(e)
        
#     return render(request,"Dashboard/addstudent.html",{"data":a,"datas":b})


# def getstudent(request):
#     k=student.objects.all()
#     print(k)
#     if request.method=="POST":
#         se=request.POST.get('name')
#         res=teachers.objects.filter(name=se)
#         return render(request,"Dashboard/slist.html",{"data":res})
#     return render(request,"Dashboard/slist.html",{"data":k})

# def getstudent_admin(request):
#     k=student.objects.all()
#     print(k)
#     return render(request,"Dashboard/admin_viewstudent.html",{"data":k})


# def delstudent(request,userid):
#     o=student.objects.get(id=userid)
#     o.delete()
#     return redirect("st")

# def update_student(request,userid):
#     x=student.objects.filter(id=userid).values()
#     k=department.objects.all()
#     if request.method=="POST":
#         F=request.POST.get('f_name')
#         L=request.POST.get('l_name')
#         M=request.POST.get('mobile')
#         E=request.POST.get('email') 
#         D=request.POST.get('department')
#         P=request.POST.get('password')  
#         x.update(fname=F,lname=L,mob=M,em=E,dname=D,pas=P)
#         return redirect("st")
#     return render(request,"Dashboard/studedit.html",{"userdata":x[0],"id":userid,"data":k})
    
# def getview(request,userid):
#     k=student.objects.filter(tuitor__email=userid)
#     print(k)
#     return render(request,"tables.html",{"data":k})

# def searchstud(request,userid):
#     k=student.objects.filter(tuitor__email=userid)
#     if request.method=="POST":
#         se=request.POST.get('name')
#         res=student.objects.filter(fname=se,tuitor__email=userid)
#         return render(request,"tables.html",{"data":res})
#     return render(request,"tables.html",{"data":k})


# def videoadd(request):
#     a=department.objects.all()
#     if request.method=='POST':
#         p=request.FILES['video']
#         fo=FileSystemStorage()
#         v2=fo.save(p.name,p)
#         D=request.POST.get('department')
#         s=request.POST.get('sem')
#         de=department.objects.get(id=D)
#         videos.objects.create(vi=v2,sem=s,depname=de)
#     return render(request,"Dashboard/videos.html",{"data":a})
