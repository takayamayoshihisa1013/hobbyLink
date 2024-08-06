from django.shortcuts import render, redirect
from .models import User

from django.contrib.auth import authenticate, login as auth_login

# データベースに湯z－ザーが存在するか確認できるものらしい
from django.contrib.auth import authenticate, login
from django.contrib import messages

# djangoのデータベースのエラーに使うもの？
from django.db import IntegrityError

import uuid

# Create your views here.


def login(request):
    user_data = "get"
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(email, password)
        
        try:
            user_data = User.objects.get(email=email, password=password)
            print(user_data)
            request.session['user_id'] = str(user_data.user_id)
            request.session["user_name"] = user_data.user_name
            return redirect("/hobbyLink/")
        except User.DoesNotExist:
            print("ない")
            user_data = None
        
    context = {
        "user_data": user_data
    }
        
    return render(request, 'login.html', context)

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


