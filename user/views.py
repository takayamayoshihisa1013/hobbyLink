from django.shortcuts import render, redirect
from .models import User

# djangoのデータベースのエラーに使うもの？
from django.db import IntegrityError

import uuid

# Create your views here.


def login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

    return render(request, "login.html")


def signup(request):
    error = False

    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            new_user = User(
                user_name=user_name,
                email=email,
                password=password
            )
            new_user.save()
            return redirect("login")  # リダイレクトのURL名を修正
        except IntegrityError as e:
            if e.args[0] == 1062:  # メールアドレスのユニーク制約違反の場合
                error = True
            else:
                raise e  # その他のエラーは再度発生させる

    context = {
        "error": error
    }
    return render(request, "signup.html", context)


