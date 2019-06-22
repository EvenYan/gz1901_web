from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from blog.models import Post


def index(request):
    # print(request.path)
    # print(request.method)
    # print(request.GET)
    # print(request.encoding)
    # print(request.COOKIES)
    post_list = Post.objects.all()
    print(post_list)
    context = {"post_list": post_list}
    return render(request, "index.html", context)


def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    print(post)
    context = {"post": post}
    return render(request, 'detail.html', context)


def new_post(request):
    return render(request, "new_post.html")


def save_post(request):
    title = request.POST.get("title")
    body = request.POST.get("body")
    Post.objects.create(title=title, body=body)
    return HttpResponse("文章保存成功！")


def get_para(request):
    para1 = request.GET.getlist("username")
    para2 = request.GET.get("passwd")
    print(para1, para2)
    return HttpResponse("参数获取成功")


def ret_response(request):
    response = HttpResponse()
    response.content = "Hello Django"
    response.write("I'm fine!")
    response.status_code = 302
    return response


def to_other_url(request):
    return redirect(reverse("blog:post", args=(1,)))

