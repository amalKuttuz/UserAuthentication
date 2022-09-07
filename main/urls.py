from django.contrib import admin
from django.urls import path
from main.views import* 
urlpatterns = [

    path('',home,name="home"),
    path('signin',signin,name="signin"),
    path('signup',signup,name="signup"),
    path('userdashboard',userdashboard,name="userdashboard"),
    path('signout',signout,name="signout")
]