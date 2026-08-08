from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import SignupForm


# Create your views here.
def login_views(request):
    if request.user.is_authenticated:
        return redirect('app:index')
    else:
        if request.method == 'POST':
            
            username_or_email = request.POST.get('username')
            password = request.POST.get('password')
            if "@" in username_or_email:
                try:
                    user_obj = User.objects.filter(email=username_or_email).first()

                    if user_obj:
                        username = user_obj.username
                    else:
                         username = None
                         
                except User.DoesNotExist:
                    username = None
            else:
                username = username_or_email
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in.")
                return redirect('app:index')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('accounts:login')

            
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout_views(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('app:index')

def signup_views(request):

    if request.user.is_authenticated:
        return redirect("website:index")

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created user.")
            return redirect("accounts:login")

        messages.error(request, "Please correct the errors below.")

    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


def password_reset_form_views(request):

    if request.method == "POST":

        username_or_email = request.POST.get("username")
        new_password = request.POST.get("password")

        try:
            if "@" in username_or_email:
                user = User.objects.get(email=username_or_email)
            else:
                user = User.objects.get(username=username_or_email)

            user.set_password(new_password)
            user.save()

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("accounts:login")

        except User.DoesNotExist:
            messages.error(
                request,
                "User not found."
            )

    return render(
        request,
        "accounts/password_reset_form.html"
    )
