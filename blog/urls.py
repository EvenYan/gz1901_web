"""gz1901_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)', views.post, name="post"),
    url(r'^index', views.index, name="index"),
    url(r'^new_post', views.new_post, name="new_post"),
    url(r'^save_post', views.save_post, name="save_post"),
    url(r'^get_para', views.get_para, name="get_para"),
    url(r'^ret_response', views.ret_response, name="ret_response"),
    url(r'^to_post', views.to_other_url, name="to_post"),
]
