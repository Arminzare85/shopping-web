from django.contrib import admin
from django.urls import path , include
from accounts.views import *
from .views import login_views

app_name =  'accounts'

urlpatterns = [
    
    path("login/",login_views,name="login"),
    path("logout/",logout_views,name="logout"),
    path("signup/",signup_views,name="signup"),
     
]