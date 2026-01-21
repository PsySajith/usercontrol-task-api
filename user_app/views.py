from django.shortcuts import render, redirect

from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'], 
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.is_active = False
            user.save()
            messages.success(request, "Wait for admin approval")
            return redirect('login')
        return render(request, "register.html", {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    messages.error(request, "Admin approval required")
            else:
                messages.error(request, "Invalid credentials")
        form = LoginForm()
        return render(request, "login.html", {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("login")



def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')
