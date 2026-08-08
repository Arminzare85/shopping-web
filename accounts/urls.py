from django.contrib import admin
from django.urls import path , include
from accounts.views import *
from .views import login_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name =  'accounts'

urlpatterns = [
    
    path("login/",login_views,name="login"),
    path("logout/",logout_views,name="logout"),
    path("signup/",signup_views,name="signup"),
    path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy("accounts:password_reset_done")
    ),
    name="password_reset",
),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
    "reset/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy("accounts:password_reset_complete")
    ),
    name="password_reset_confirm",
),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
   
    

     
]