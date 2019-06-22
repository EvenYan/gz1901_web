from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print("执行MyMiddleware1的process_request方法！")
        # return HttpResponse("提前返回")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行MyMiddleware1的process_view方法！")

    def process_response(self, request, response):
        print("执行MyMiddleware1的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行MyMiddleware1的process_exception方法！")

    def process_template_response(self, request, response):
        print("执行MyMiddleware1的process_template_response方法！")


class MyMiddleware２(MiddlewareMixin):
    def process_request(self, request):
        print("执行MyMiddleware2的process_request方法！")
        # return HttpResponse("提前返回")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行MyMiddleware２的process_view方法！")

    def process_response(self, request, response):
        print("执行MyMiddleware２的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行MyMiddleware2的process_exception方法！")

    def process_template_response(self, request, response):
        print("执行MyMiddleware２的process_template_response方法！")


block_ip_list = ["192.168.159.139"]


class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        remote_ip = request.META.get("REMOTE_ADDR")
        print(remote_ip)
        if remote_ip in block_ip_list:
            print("BlockIPMiddleware的process_request方法！")
            return HttpResponse("你的IP被禁止了！")
