from django.contrib import admin
from django.urls import path , include
from app.views import *

app_name =  'app'

urlpatterns = [
    
    path("",home_views,name="index"),
    path("shop/",shop_views,name="shop"),
    path("single/<int:pid>/",single_views,name="single"),
    path("bestseller/",bestseller_views,name="bestseller"),
    path("cart/",cart_views,name="cart"),
    path("cheackout/",cheackout_views,name="cheackout"),
    path("404/",fourzero_views,name="404"),
    path("contact/",contact_views,name="contact"),
    path("search/", search_views, name="search"),

     
]