from django.contrib import admin
from django.urls import path
from page1 import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("author",views.author,name="home"),
    path("userdashboard/issuebooks",views.issuebooks,name="issuebooks"),
    path("landing",views.landing,name="landing"),
    path("userdashboard/publishbook",views.publishbook,name="publishbook"),
    path("register",views.register,name="register"),
    path("userdashboard/returnbook",views.returnbook,name="returnbook"),
    path("review",views.review,name="review"),
    path("userdashboard/signin",views.signin,name="signin"),
    path("userdashboard",views.userdashboard,name="userdashboard"),

]