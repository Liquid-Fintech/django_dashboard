from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import auth, User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import AuthenticationForm


class RegisterView(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register was successful')
            return redirect('home')
        else:
            messages.success(request, 'Register was not successful')
            return redirect('register')


@login_required()
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout was successful')
    return redirect('home')


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Login was successful')
            return redirect('home')
        else:
            messages.error(request,
                           'login was not successful please make sure you are writing right username and passsword ')
            return redirect('login')
