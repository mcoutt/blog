
class NewsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        message = "<! - HelloWorld >>"
        response = self.get_response(request)
        print(message)
        response['X-My-Header'] = message
        return response
