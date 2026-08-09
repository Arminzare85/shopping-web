from django.contrib import admin
from django.urls import path , include
from store.views import *
from app.views import wishlist_views

app_name =  'store'

urlpatterns = [
    
    path("toggle_wishlist/<int:product_id>/",toggle_wishlist,name="toggle_wishlist"),
    path("wishlist/",wishlist_views,name="wishlist"),
    path("delete_wishlist/<int:product_id>/",delete_wishlist,name="delete_wishlist"),
    
]
