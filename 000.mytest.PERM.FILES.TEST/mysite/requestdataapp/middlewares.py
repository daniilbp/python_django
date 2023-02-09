import datetime
from datetime import timedelta
from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):

    print('Initial call')

    def middleware(request: HttpRequest):
        print('before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('after get response')
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.last_user_ip = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print('requests count', self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print('responses count', self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exception so far')


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.timeout = timedelta(seconds=0)
        self.req_info = {}

    def __call__(self, request: HttpRequest):
        req_ip = str(request.META['REMOTE_ADDR'])
        print('---IP---', req_ip)
        print('Dict --- ', self.req_info)
        print('Timeout ===', self.timeout)
        req_time = datetime.datetime.now()
        if not self.req_info:
            self.req_info[req_ip] = req_time
        elif self.req_info[req_ip]:
            if self.req_info[req_ip] >= req_time - self.timeout:
                raise TimeoutError('Time between requests short (< 0 sec) ')
        self.req_info[req_ip] = req_time
        response = self.get_response(request)
        return response
