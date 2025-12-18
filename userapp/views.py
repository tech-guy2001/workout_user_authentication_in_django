from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"home.html")


def aboutpage(request):
    return render(request,"about.html")

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email    = request.POST.get("email")
        password = request.POST.get("password")
        confirm  = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created. Please log in.")
        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # Important: this simply creates a session for this device/browser.
            # It DOES NOT log out other sessions, so multi-device login is allowed.
            login(request, user)
            print(user)
            return redirect(home)  # change to your home/dashboard
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")
    return render(request, "login.html")


def logout_view(request):
    logout(request)  # logs out the current session only
    messages.success(request, "Logged out.")
    return redirect("login")
