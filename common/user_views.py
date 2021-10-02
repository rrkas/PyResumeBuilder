from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from common.forms import RegisterUserForm, EmailLoginForm


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful! You can login now!")
            return redirect("login")
    form = RegisterUserForm()
    return render(request, "users/register.html", context={"user_form": form})


class EmailLoginView(LoginView):
    authentication_form = EmailLoginForm
