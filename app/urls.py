from django.contrib import admin
from django.urls import path , include
from app.views import *

app_name =  'app'

urlpatterns = [
    
    path("",home_views,name="index"),
     
]