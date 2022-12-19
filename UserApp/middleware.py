import time


class DisableSessionCSRF:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request._dont_enforce_csrf_checks = True
        response = self.get_response(request)
        print(response)
        time.sleep(2)
        return response
