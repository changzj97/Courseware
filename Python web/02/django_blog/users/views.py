from django.shortcuts import render, reverse, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import BlogUser
from django.contrib.auth.hashers import make_password


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = BlogUser()
        user.username = username
        user.password = make_password(password)
        user.email = email
        user.is_active = True

        user.save()

        return render(request, 'login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 从前端取出来的数据
        username = request.POST.get('username', default='')
        password = request.POST.get('password', '')
        # 拿着前端取出来的数据去 数据库验证
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                # django 的视图函数
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return render(request, 'login.html', {'error_msg': '用户未激活'})

        else:
            return render(request, 'login.html', {'error_msg': '用户名或者密码错误'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
