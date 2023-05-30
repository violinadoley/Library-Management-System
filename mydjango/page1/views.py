from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from page1.models import BookIssue,BookPublish,BookReview,Author
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def author(request):
    return render(request,'author.html')

def issuebooks(request):
    return render(request,'issuebooks.html')

def issuebooks(request):
    if request.method == "POST":
        booktitle = request.POST.get('booktitle')
        authorname = request.POST.get('authorname')
        ISBN = request.POST.get('ISBN')

        issue = BookIssue(booktitle= booktitle,authorname = authorname,ISBN = ISBN,date = datetime.today())
        issue.save()
    return render(request,'review')

def landing(request):
    return render(request,'landing.html')

def publishbook(request):
    if request.method == "POST":
        authorname = request.POST.get('authorname')
        booktitle = request.POST.get('booktitle')
        ISBN = request.POST.get('ISBN')
        desc = request.POST.get('desc')
        publ = BookPublish(authorname = authorname,booktitle = booktitle,desc= desc,ISBN= ISBN,publdate= datetime.today())
        publ.save()

        return HttpResponse("Book Published!")
    return render(request,'publishbook.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        email = request.POST.get['email']
        myuser = User.objects.create_user(username,password,email)
        myuser.name= username
        
        myuser.save()

        messages.success(request,"Account successfully created!")
        return redirect('signin.html')
    return render(request,'register.html')

def returnbook(request):
    return render(request,'returnbook.html')

def review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        booktitle = request.POST.get('booktitle')
        review = request.POST.get('review')

        rev = BookReview(name = name,booktitle = booktitle,review= review,date = datetime.today())
        rev.save()

        return HttpResponse("Review Added!")
    return render(request,'review.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        myuser = User.objects.create(username,password)
        myuser.name= username
        
        myuser.save()

        messages.success(request,"Account successfully created!")
        return redirect('home')
    return render(request,'signin.html')
        
    

def userdashboard(request):
    
    return render(request,'userdashboard.html')
