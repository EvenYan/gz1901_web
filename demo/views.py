import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from demo.models import UserInfo


def index(request):
    context = {"str": "<script>alert('Hi')</script>"}
    return render(request, "demo/home.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        print(username, passwd)
        request.session['username'] = username
        passwd = get_sec_passwd(passwd)
        user = UserInfo.objects.filter(username=username).filter(passwd=passwd)
        if user:
            print(username)
            print(passwd)
            response = HttpResponse("登录成功")
            # response.delete_cookie("name")
            return response
        return HttpResponse("输入的账号或者密码错误！")
    return render(request, "demo/homepage.html")


def home(request):
    username= request.session.get("username")
    context = {"username": username}
    return render(request, 'homepage.html', context)


def homepage(request):
    return render(request, 'demo/homepage.html')


def get_sec_passwd(passwd):
    sha = hashlib.sha512()
    sha.update(passwd.encode())
    return sha.hexdigest()


def register(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    passwd = request.POST.get("passwd")
    passwd_confirm = request.POST.get("passwd_confirm")
    if passwd == passwd_confirm:
        print(username, email, passwd, passwd_confirm)
        user = UserInfo()
        user.username = username
        passwd = get_sec_passwd(passwd)
        user.passwd = passwd
        user.email = email
        user.save()
        return redirect(reverse("demo:login"))
    return HttpResponse("两次密码不一致，请重新注册！")